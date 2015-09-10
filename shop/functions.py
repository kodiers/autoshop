# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0

import sys
import os
import random
import xlrd
import xlsxwriter
from autoshop.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.models import Group, User
from django.http import HttpResponseForbidden
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader
from django.db.models import Q

from shop.models import Goods, PriceList, Supplier, Markup, Orders, OrderDetails, Clients, Developer, \
    ClientsPriceCategory


def create_password_str():
    """
    This function generate 8-length random password from numbers and letters
    """
    symbols = '1 2 3 4 5 6 7 8 9 0 Q W E R T Y U I O P A S D F G H J K L Z X C V B N M q w e r t y u i o p a s d f g h j k l z x c v b n m'
    sym_list = symbols.split()
    password_list = random.sample(sym_list, 8)
    password = ''.join(password_list)
    return password


def check_admin_group(request, group_name):
    """
    This function check if logged user is administrator
    """
    group = Group.objects.get(name=group_name)
    if group in request.user.groups.all() or request.user.is_superuser:
        return True
    else:
        return False


def raise_403(request):
    """
    Render custom 403 http error page
    """
    t = loader.get_template("mgmt/403.html")
    cont = RequestContext(request)
    cont.update(csrf(request))
    return HttpResponseForbidden(t.render(cont))


def parse_pricelist(file):
    """
    Parse price list.
    Get filepath, and return list of lists, where first list is list of columns headers (first row in sheet),
    and all others rows are data in the sheet.
    """
    workbook = xlrd.open_workbook(file)
    xl_sheet = workbook.sheet_by_index(0)
    header_row = xl_sheet.row(0)
    header = []  # List of cell in first row in the sheet (Headers)
    cell_data = []  # List of cell in row (data)
    row_data = []  # List of cell_data
    for cell in header_row:
        header.append(cell.value)
    num_cols = xl_sheet.ncols
    for row_num in range(1, xl_sheet.nrows):
        xl_sheet.row(row_num)
        for col in range(0, num_cols):
            cell = xl_sheet.cell(row_num, col)
            # Convert partnumber (first column) and remainder (third column) to string
            if xl_sheet.cell_type(row_num, col) == xlrd.XL_CELL_NUMBER:
                if col == 1 or col == 5:
                    str_value = str(int(cell.value))
                    cell_data.append(str_value)
                else:
                    cell_data.append(cell.value)
            else:
                cell_data.append(cell.value)
        row_data.append(cell_data)
        cell_data = []
    del workbook
    return header, row_data


def calculate_price(goods, markup):
    """
    Calculate price and save in database
    :param goods: - list of goods
    :param markup: - markup
    :return: price as float
    """
    for good in goods:
        good.price = round((float(good.cost) * ((100 + float(markup)) / 100)), 2)
        good.save()


def insert_pricelist_data(price_file, delivery_time=0, markup=0, price_ip=0, price_ltd=0):
    """
    Insert data in database. Create goods and markup objects.
    :param price_file: pricelist name
    :param markup: markup for this price, default 1
    :param delivery_time: delivery time for goods in this price, default 1
    :param price_ip: price for category with code "ip"
    :param price_ltd: price for category with code "ltd"

    """
    pricelist = PriceList.objects.get(file=price_file)
    data = parse_pricelist(pricelist.file.path)
    supplier = Supplier.objects.get(pk=pricelist.supplier_id)
    # developers_list = Developer.objects.all()
    if markup == '':
        markup = 0
    if price_ltd == '':
        price_ltd = 0
    if price_ip == '':
        price_ip = 0
    if delivery_time == '':
        delivery_time = 0
    if markup != 0:
        # Create markup object
        markup_object = Markup()
        markup_object.title = supplier.title + " " + pricelist.__str__()
        markup_object.pricelist = pricelist
        markup_object.suppliers = supplier
        markup_object.value = float(markup)
        markup_object.save()
    # Delete old goods from this supplier
    Goods.objects.filter(supplier=supplier).delete()
    # while Goods.objects.filter(supplier=supplier).count():
    # Goods.objects.filter(supplier=supplier)[0].delete()
    goods = data[1]
    # Create new goods from price list data
    for good in goods:
        object_good = Goods()
        object_good.title = good[2]
        object_good.partnumber = good[1]
        object_good.remainder = good[5]
        object_good.cost = good[6]
        object_good.internal_partnumber = good[3]
        # This code check and create developer. Need testing on real webserver
        object_good.developer = Developer.objects.get_or_create(title=good[4])[0]
        object_good.price_list = pricelist
        object_good.supplier = supplier
        object_good.delivery_time = delivery_time
        object_good.price = round((float(good[6]) * ((100 + float(markup)) / 100)), 2)
        object_good.price_ip = round((float(good[6]) * ((100 - float(price_ip)) / 100)), 2)
        object_good.price_org = round((float(good[6]) * ((100 - float(price_ltd)) / 100)), 2)
        object_good.save()


def change_markup(form):
    """
    Change markup. Get form object and return True (no errors) or False (some error)
    :param form: form object
    :return: boolean value (true if no errors)
    """
    supplier = form.cleaned_data['suppliers']
    pricelist = form.cleaned_data['pricelist']
    goods_category = form.cleaned_data['goods_category']
    developer = form.cleaned_data['developer']
    value = form.cleaned_data['value']
    # Change markup for defined attributes
    try:
        if supplier is not None:
            goods = Goods.objects.filter(supplier=supplier)
            calculate_price(goods, value)
        if pricelist is not None:
            goods = Goods.objects.filter(price_list=pricelist)
            calculate_price(goods, value)
        if goods_category is not None:
            goods = Goods.objects.filter(category=goods_category)
            calculate_price(goods, value)
        if developer is not None:
            goods = Goods.objects.filter(developer=developer)
            calculate_price(goods, value)
        return True
    except:
        return False


def calculate_stock(stock):
    """
    Calculate stock value for goods.
    :param stock: object of stock
    :return: boolean value (true if no errors)
    """
    stock_value = stock.value
    goods_category = stock.goods_category
    developer = stock.developer
    try:
        if goods_category is not None:
            goods = Goods.objects.filter(category=goods_category)
            for good in goods:
                good.stock = stock
                good.stock_price = round(float(good.price) * ((100 - float(stock_value)) / 100), 2)
                good.save()
        if developer is not None:
            goods = Goods.objects.filter(developer=developer)
            for good in goods:
                good.stock = stock
                good.stock_price = round(float(good.price) * ((100 - float(stock_value)) / 100), 2)
                good.save()
        return True
    except:
        return False


def check_attribute(attribute):
    """
    Check if attribute is exist
    :param attribute: attribute of models to check
    :return: return "N/A or attribute.title
    """
    if attribute is None:
        return "N/A"
    else:
        return attribute.title


def export_goods_to_excel(filepath):
    """
    Export goods to excel file from database
    :param filepath: path to file for save
    :return: boolean value: true if no error, false if some errors
    """
    # Need for fix unicode error
    reload(sys)
    sys.setdefaultencoding('utf-8')
    goods = Goods.objects.all()
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()
    bold_text = workbook.add_format({'bold': True})
    try:
        row_num = 0
        headers = ["Артикул", "Название", "Категория", "Производитель", "Поставщик", "Остаток на складе",
                   "Зарезервировано", "Ед. изм.", "Время доставки", "Цена", "Стоимость",
                   "Цена по акции", "Акция"]
        # write headers
        for head in range(len(headers)):
            worksheet.write(row_num, head, headers[head].decode('utf-8'), bold_text)

        # write positions
        for good in goods:
            row_num += 1
            row = [good.partnumber.encode('utf-8'), good.title.encode('utf-8'),
                   check_attribute(good.category).encode('utf-8'), check_attribute(good.developer).encode('utf-8'),
                   check_attribute(good.supplier).encode('utf-8'), good.remainder, good.reserved,
                   good.meassure.encode('utf-8'), good.delivery_time,
                   good.price, good.cost, good.stock_price, check_attribute(good.stock).encode('utf-8')]
            for col_num in range(len(row)):
                worksheet.write(row_num, col_num, row[col_num])

        workbook.close()

        return True
    except:
        workbook.close()
        return False


def delete_order_detail(order_detail, order):
    """
    Delete order detail and set reserved goods and remainder goods also change total order sum
    :param order_detail: OrderDetail object
    :return: True if no errors
    """
    try:
        try:
            good = Goods.objects.get(pk=order_detail.goods_id)
        except ObjectDoesNotExist:
            good = Goods.objects.get(partnumber=order_detail.goods_pn)
        good.reserved = good.reserved - order_detail.quantity
        good.remainder = good.remainder + order_detail.quantity
        order.order_sum = round((order.order_sum - order_detail.total_goods_price), 2)
        order.save()
        good.save()
        order_detail.delete()
        return True
    except:
        return False


def check_goods_remainder(good):
    """
    Check quantity of goods
    :param good: Goods object
    :return: False if good.quantity <= 0
    """
    if good.remainder <= 0:
        return False
    else:
        return True


def orders_to_excel(file_path):
    """
    Export orders to excel
    :param file_path: path to file for export
    :return: True if no errors, except False
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    orders = Orders.objects.all()
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    bold_text = workbook.add_format({'bold': True})
    try:
        row_num = 0
        headers = ["Номер заказа", "Номер клиента", "Клиент", "Артикул", "Производитель", "Позиция",
                   "Количество", "Цена", "Общая сумма заказа", "Статус заказа", "Статус оплаты"]
        for head in range(len(headers)):
            worksheet.write(row_num, head, headers[head].decode('utf-8'), bold_text)
        for order in orders:
            order_details = OrderDetails.objects.filter(order=order)
            for detail in order_details:
                row_num += 1
                good = Goods.objects.get(partnumber=detail.goods_pn)
                payments_status = 'Не оплачен'
                if order.payment_status:
                    payments_status = "Оплачен"
                row = [order.pk, order.client.pk, order.client.title.encode('utf-8'), detail.goods_pn.encode('utf-8'),
                       check_attribute(good.developer), detail.goods.encode('utf-8'), detail.quantity,
                       detail.goods_price,
                       order.order_sum, order.get_status_display(), payments_status.decode('utf-8')]
                for col_num in range(len(row)):
                    worksheet.write(row_num, col_num, row[col_num])
        workbook.close()
        return True
    except:
        workbook.close()
        return False


def search_goods_func(word, price_opt=None):
    """
    Search goods function
    :param word: what to search (partnumber or word)
    :return: Lists of goods
    """
    word_no_space = word.lstrip().rstrip()
    cap_word = word.upper().lstrip().rstrip()
    without_space_defic_str = word.lstrip().rstrip().replace('-', '')
    without_space_defic_str_cap = cap_word.lstrip().rstrip().replace('-', '')
    if price_opt is None or price_opt == False:
        price_opt = False
        objects = Goods.objects.filter(Q(title__contains=word_no_space) | Q(description__contains=word_no_space) |
                                   Q(partnumber__contains=word_no_space) |
                                   Q(title__contains=cap_word) | Q(description__contains=cap_word) |
                                   Q(partnumber__contains=without_space_defic_str)
                                   | Q(partnumber__contains=without_space_defic_str_cap)).filter(price_list__opt=price_opt).order_by('delivery_time', 'price')
    else:
        objects = Goods.objects.filter(Q(title__contains=word_no_space) | Q(description__contains=word_no_space) |
                                   Q(partnumber__contains=word_no_space) |
                                   Q(title__contains=cap_word) | Q(description__contains=cap_word) |
                                   Q(partnumber__contains=without_space_defic_str)
                                   | Q(partnumber__contains=without_space_defic_str_cap)).order_by('delivery_time', 'price')
    if not objects.exists():
        # If partnumber has defic or search string with not defic delete all defices and spaces and check
        obj_array = []
        if price_opt is None:
            goods = Goods.objects.all().order_by('delivery_time', 'price')
        else:
            goods = Goods.objects.filter(price_list__opt=price_opt).order_by('delivery_time', 'price')
        for good in goods:
            if without_space_defic_str == good.partnumber.lstrip().rstrip().replace('-', ''):
                obj_array.append(good)
            elif without_space_defic_str == good.partnumber.lstrip().rstrip().replace('-', ''):
                obj_array.append(good)
            elif without_space_defic_str_cap == good.partnumber.lstrip().rstrip().replace('-', ''):
                obj_array.append(good)
        return obj_array
    return objects


def check_basket_quantity(good, basket):
    """
    Check if good.remainder is less than basket.quantity. Else show warning.
    :param good: good object
    :param basket: basket object
    :return: string
    """
    if good.remainder < basket.quantity:
        return "Товара недостаточно на складе. Свяжитесь с менеджером."


def calculate_basket_total(good, basket):
    """
    Calculate basket total_price.
    :param good: Goods object
    :param basket: Basket object
    :return: float (total_price)
    """
    client = Clients.objects.get(title=basket.client.title)
    client_category = ClientsPriceCategory.objects.get(clients__login=client.login)
    if client.private_stock == 0:
        if good.stock_price != 0:
            total_price = round((good.stock_price * basket.quantity), 2)
        else:
            if client_category is not None:
                if client_category.code == "ip":
                    total_price = round((good.price_ip * basket.quantity), 2)
                elif client_category.code == "ltd":
                    total_price = round((good.price_org * basket.quantity), 2)
                else:
                    total_price = round((good.price * basket.quantity), 2)
            else:
                total_price = round((good.price * basket.quantity), 2)
    else:
        total_price = round(((good.price * basket.quantity) * ((100 - client.private_stock) / 100)), 2)
    return total_price


def calculate_basket_summ(baskets):
    """
    Calculate total sum for goods in basket with personal stock.
    :param baskets: list of baskets
    :return: float ( total sum)
    """
    total_summ = 0
    for basket in baskets:
        if basket.private_price == 0:
            total_summ += basket.total_price
        else:
            total_summ += basket.private_price
    return total_summ


def payment_received(sender, **kwargs):
    """
    Handle payment after payment is recieved.
    :param sender:
    :param kwargs:
    """
    order = Orders.objects.get(pk=kwargs['InvId'])
    order.payment_status = True
    order.save()
    client = Clients.objects.get(pk=order.client.pk)
    client.unpaid_orders -= 1
    client.unpaid_sum -= order.order_sum
    client.orders_sum += order.order_sum
    client.save()


def check_client_category(request):
    """
    Return client category if it's defined, another return None
    :param request: HttpRequest object
    :return: None or ClientPriceCategory object
    """
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.get_username())
        # client = Clients.objects.get(login=user)
        try:
            client_category = ClientsPriceCategory.objects.get(clients__login=user)
        except:
            client_category = None
    else:
        client_category = None
    return client_category


def add_photo():
    """
    Listing 'photos' directory and add images to goods.
    Image name should be equal to good.partnumber
    :return:
    """
    goods = Goods.objects.all()
    try:
        for root, dir, files in os.walk(MEDIA_ROOT + '/photos'):
            for file in files:
                for good in goods:
                    ll = len(good.partnumber)
                    if ll != 0:          # check if partnumber exists
                        if good.partnumber == os.path.splitext(file)[0]:
                            good.image = 'photos/' + file
                            good.save()
        return True
    except:
        return False


