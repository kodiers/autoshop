# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0

import datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

from robokassa.signals import result_received


# Create your models here.

class Developer(models.Model):
    """
    Developers model
    """
    title = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField(upload_to='uploads', blank=True, null=True, verbose_name='Изображение', default=None)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-title']
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Supplier(models.Model):
    """
    Supplier model
    """
    title = models.CharField(max_length=256, verbose_name='Название')
    bank_data = models.TextField(verbose_name='Банковские реквизиты', null=True, blank=True)
    law_address = models.TextField(verbose_name='Юридический адрес', null=True, blank=True)
    fact_address = models.TextField(verbose_name='Фактический адрес', null=True, blank=True)
    contact = models.TextField(verbose_name='Контактное лицо', null=True, blank=True)
    contact_phone = models.CharField(max_length=64, null=True, blank=True, verbose_name='Контактный телефон')
    contact_email = models.EmailField(null=True, blank=True, verbose_name='Контактный email')

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class PriceList(models.Model):
    """
    Price lists model
    """
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик')
    file = models.FileField(upload_to='pricelists', verbose_name='Файл')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата загрузки')
    opt = models.BooleanField(default=False, verbose_name="Прайс-лист для оптовых покупателей")

    def __unicode__(self):
        return self.date.strftime('%Y %b %d %H:%M')

    def __str__(self):
        return self.date.strftime('%Y %b %d %H:%M')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-листы'


class GoodsCategory(models.Model):
    """
    Category of goods model
    """
    title = models.CharField(max_length=128, verbose_name='Название')
    image = models.ImageField(upload_to='uploads', blank=True, null=True, verbose_name='Изображение', default=None)

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Stock(models.Model):
    """
    Stock sell model
    """
    title = models.CharField(max_length=128, verbose_name='Название', null=True, blank=True)
    goods_category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name='Категория товаров')
    developer = models.ForeignKey(Developer, null=True, blank=True, verbose_name='Производитель')
    value = models.FloatField(default=0, verbose_name='Размер скидки')
    show_on_main_page = models.BooleanField(default=False, verbose_name='Показывать на главной')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified_date']
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Goods(models.Model):
    """
    Goods model
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="Категория", blank=True, null=True,
                                 on_delete=models.SET_NULL)
    developer = models.ForeignKey(Developer, verbose_name="Производитель", blank=True, null=True,
                                  on_delete=models.SET_NULL)
    partnumber = models.CharField(max_length=128, verbose_name="Артикул", blank=True, null=True)
    internal_partnumber = models.CharField(max_length=128, verbose_name="Внутренний артикул", blank=True, null=True)
    title = models.TextField(verbose_name="Название", blank=True, null=True)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='uploads', blank=True, null=True, verbose_name="Изображение", default=None)
    show_on_index = models.BooleanField(default=False, verbose_name="Отображать на главной")
    remainder = models.IntegerField(default=0, verbose_name="Остаток на складе")
    reserved = models.IntegerField(default=0, verbose_name="Зарезервировано")
    delivery_time = models.IntegerField(default=0, verbose_name="Время доставки")
    meassure = models.CharField(max_length=64, verbose_name="Единица измерения", default="шт.")
    cost = models.FloatField(default=0.0, verbose_name="Стоимость")
    price = models.FloatField(default=0.0, verbose_name="Цена (розница)")
    price_ip = models.FloatField(default=0.0, verbose_name="Цена для категории 'индивидульный преприниматель'")
    price_org = models.FloatField(default=0.0, verbose_name="Цена для категории 'юридическое лицо'")
    supplier = models.ForeignKey(Supplier, verbose_name="Поставщик", blank=True, null=True)
    stock_price = models.FloatField(default=0.0, verbose_name="Цена по акции")
    price_list = models.ForeignKey(PriceList, verbose_name="Прайс-листы", blank=True, null=True)
    stock = models.ForeignKey(Stock, blank=True, null=True, verbose_name="Акция", on_delete=models.SET_NULL)

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class Markup(models.Model):
    """
    Sale prices model
    """
    title = models.CharField(max_length=256, blank=True, null=True, verbose_name='Название')
    suppliers = models.ForeignKey(Supplier, null=True, blank=True, verbose_name='Поставщик')
    pricelist = models.ForeignKey(PriceList, null=True, blank=True, verbose_name='Прайс-лист')
    goods_category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name='Категория товаров')
    developer = models.ForeignKey(Developer, null=True, blank=True, verbose_name='Производитель')
    value = models.FloatField(default=0, verbose_name='Размер наценки')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified_date']
        verbose_name = 'Торговая наценка'
        verbose_name_plural = 'Наценки'


class Export1C(models.Model):
    """
    Export data files to 1C model
    """
    EXPORT_TYPE = (
        (0, 'Goods'),
        (1, 'Orders')
    )
    title = models.CharField(max_length=128, verbose_name='Название', null=True, blank=True)
    file = models.TextField(verbose_name='Файл', null=True, blank=True)  # Contains path to export file (mb should change on FilePathField)
    url = models.SlugField(null=True, blank=True, verbose_name='URL')
    type = models.IntegerField(choices=EXPORT_TYPE, default=0, verbose_name='Тип выгрузки')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата выгрузки')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'Выгрузка остатков в 1С'
        verbose_name_plural = 'Выгрузки'


# ------------- Fixes bug 17.04.2015 ------------------------------------------
class ClientsPriceCategory(models.Model):
    """
    Clients category
    """
    title = models.CharField(verbose_name="Название категории", max_length=256)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    code = models.CharField(verbose_name="code", max_length=128, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории цены"
        verbose_name = "Категория цены"

# ------------ end fixing ------------------------------------------------------

class Clients(models.Model):
    """
    Client's model
    """
    PAYMENTS = (
        (0, 'Наличными'),
        (1, 'Электронным платежом'),
        (2, 'По счету'),
    )
    login = models.ForeignKey(User, verbose_name='Логин')
    title = models.CharField(max_length=256, verbose_name='Название')
    contact_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Контактное имя')
    contact_address = models.TextField(null=True, blank=True, verbose_name='Контактный адрес')
    contact_phone = models.CharField(max_length=128, null=True, blank=True, verbose_name='Контактный телефон')
    contact_email = models.EmailField(verbose_name='Контактный email')
    law_data = models.TextField(verbose_name='Юридические данные организации', null=True, blank=True)
    law_address = models.TextField(verbose_name='Юридический адрес организации', null=True, blank=True)
    is_org = models.BooleanField(default=False,
                                 verbose_name='Организационная форма')  # If False, then client is private person
    clients_category = models.ForeignKey(ClientsPriceCategory, verbose_name="Категория цены", null=True, blank=True)
    delivery_zip = models.CharField(max_length=128, null=True, blank=True, verbose_name="Почтовый индекс адреса доставки")
    delivery_city = models.CharField(max_length=128, null=True, blank=True, verbose_name="Город доставки")
    delivery_street = models.TextField(null=True, blank=True, verbose_name="Улица доставки")
    delivery_home = models.CharField(null=True, blank=True, verbose_name="Номер и корпус дома доставки", max_length=128)
    delivery_office = models.CharField(max_length=128, blank=True, null=True, verbose_name="Номер квартиры/офиса")
    preferred_payments = models.IntegerField(choices=PAYMENTS, default=0, verbose_name='Предпочитаемый метод платежа')
    private_stock = models.FloatField(default=0, verbose_name='Размер личной скидки')
    orders_sum = models.FloatField(default=0, verbose_name='Общая сумма заказов')
    unpaid_orders = models.IntegerField(default=0, verbose_name='Количество неоплаченных заказов')
    unpaid_sum = models.FloatField(default=0, verbose_name='Задолженность')
    registration_date = models.DateField(default=timezone.now, verbose_name='Дата регистрации')

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class DeliveryMethods(models.Model):
    """
    Delivery methods model
    """
    title = models.CharField(max_length=128, verbose_name="Название")
    description = RichTextField(verbose_name="Описание", null=True, blank=True)
    cost = models.FloatField(verbose_name="Стоимость", null=True, blank=True)
    id_method = models.CharField(max_length=32, verbose_name="ID", null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Метод доставки"
        verbose_name_plural = "Методы доставки"


class PaymentsMethods(models.Model):
    """
    Payments method model
    """
    title = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(max_length=128, verbose_name="Описание")
    id_method = models.CharField(max_length=32, verbose_name="ID") # For programming only

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Метод платежа"
        verbose_name_plural = "Методы платежа"

class Orders(models.Model):
    """
    Orders model.
    Default 'id' field is orders number
    """
    ORDER_STATUS = (
        (0, 'Получен'),
        (1, 'В обработке'),
        (2, 'Сформирован'),
        (3, 'Отправлен'),
        (4, 'Отклонен'),
        (5, 'Выдано')
    )
    client = models.ForeignKey(Clients, verbose_name='Клиент')
    order_sum = models.FloatField(default=0, verbose_name='Сумма заказа')
    delivery_zip = models.CharField(max_length=128, null=True, blank=True, verbose_name="Почтовый индекс адреса доставки")
    delivery_city = models.CharField(max_length=128, null=True, blank=True, verbose_name="Город доставки")
    delivery_street = models.TextField(null=True, blank=True, verbose_name="Улица доставки")
    delivery_home = models.CharField(null=True, blank=True, verbose_name="Номер и корпус дома доставки", max_length=128)
    delivery_office = models.CharField(max_length=128, blank=True, null=True, verbose_name="Номер квартиры/офиса")
    status = models.IntegerField(choices=ORDER_STATUS, default=0, verbose_name='Статус заказа')
    payment_status = models.BooleanField(default=False,
                                         verbose_name='Статус платежа')  # If False, then order is not paid
    payments = models.ForeignKey(PaymentsMethods, verbose_name="Метод платежа")
    delivery = models.ForeignKey(DeliveryMethods, verbose_name="Метод доставки", null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания заказа')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')
    comments = models.TextField(null=True, blank=True, verbose_name='Комментарии')

    def __unicode__(self):
        return unicode(self.id)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-modified_date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderDetails(models.Model):
    """
    Order detail order.
    This model doesn't have relationships with model Goods because data in Goods database table can change,
    but order history shouldn't change.
    """
    order = models.ForeignKey(Orders, verbose_name='Заказ')
    goods = models.TextField(max_length=128, verbose_name='Товар')  # Contains goods title
    goods_pn = models.CharField(max_length=128, verbose_name='Арктикул')  # Contains goods partnumber
    goods_id = models.IntegerField(null=True, blank=True, verbose_name='ID товара') # Contains pk of good
    quantity = models.IntegerField(verbose_name='Количество')  # Contains quantity of goods
    meassure = models.CharField(max_length=128, verbose_name='Ед. измерения', null=True, blank=True)
    goods_price = models.FloatField(
        verbose_name='Цена за единицу')  # Contains goods price for client at the day of order
    total_goods_price = models.FloatField(verbose_name='Общая цена')

    def save(self):
        # need custom save method, for calculate total_goods_price
        self.total_goods_price = self.goods_price * self.quantity
        super(OrderDetails, self).save()

    def __unicode__(self):
        return str(self.order)

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'


class Bills(models.Model):
    """
    Bills model.
    Default 'id' field is order number
    """
    client = models.ForeignKey(Clients, verbose_name='Клиент')
    order = models.ForeignKey(Orders, verbose_name='Номер заказа')
    created_date = models.DateField(default=timezone.now, verbose_name='Дата создания')
    modified_date = models.DateField(default=timezone.now, verbose_name='Дата изменения')
    bill_status = models.BooleanField(default=False, verbose_name='Статус счета')  # If False, then bill is not paid
    comments = models.TextField(null=True, blank=True, verbose_name='Комментарии')

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class Pages(models.Model):
    """
    Pages class
    """
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    url = models.SlugField(verbose_name='Относительный URL')
    content = RichTextField(verbose_name='Текст')
    image = models.ImageField(upload_to='uploads', blank=True, null=True, verbose_name='Изображение', default=None)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def get_absolute_url(self):
        return '/pages/' + self.URL

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified_date']
        verbose_name = 'Страница сайта'
        verbose_name_plural = 'Страницы сайта'


class FAQ(models.Model):
    """
    Frequently asked questions model
    """
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def __unicode__(self):
        return u'%s' % self.question

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-modified_date']
        verbose_name_plural = 'FAQ'


class Contacts(models.Model):
    """
    Contacts class
    """
    phone = models.CharField(max_length=128, verbose_name='Телефон')
    zip = models.CharField(max_length=12, verbose_name='Почтовый индекс')
    address = models.CharField(max_length=128, verbose_name='Адрес')
    email = models.EmailField(default='test@test.ru')
    map = models.CharField(max_length=256, blank=True, null=True, verbose_name='Скрипт карты')
    comments = models.TextField(null=True, blank=True, verbose_name='Комментарии')

    class Meta:
        verbose_name_plural = 'Контакты'

    def __unicode__(self):
        return u'Контакты'

    def __str__(self):
        return u'Контакты'


class AboutCompany(models.Model):
    """
    Info about company
    """
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Текст')
    bank_name = models.TextField(verbose_name='Название банка', null=True, blank=True)
    inn = models.CharField(verbose_name='ИНН', max_length=128, null=True, blank=True)
    kpp = models.CharField(verbose_name='КПП', max_length=128, null=True, blank=True)
    bik = models.CharField(verbose_name='БИК', max_length=128, null=True, blank=True)
    company_name = models.TextField(verbose_name='Название компании', null=True, blank=True)
    kor_account = models.CharField(verbose_name='Корреспондентский счет', null=True, blank=True, max_length=128)
    account = models.CharField(verbose_name='Расчетный счет', null=True, blank=True, max_length=128)
    reg_data = models.TextField(verbose_name='Сведения о регистрации', null=True, blank=True)
    law_address = models.TextField(verbose_name='Юридический адрес', null=True, blank=True)
    ceo = models.TextField(verbose_name='Генеральный директор', null=True, blank=True)
    buh = models.TextField(verbose_name='Главный бухгалтер', null=True, blank=True)
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class ForSuppliers(models.Model):
    """
    Info for partners
    """
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Текст')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщикам'
        verbose_name_plural = 'Поставщикам'


class DeliveryInfo(models.Model):
    """
    Info about delivery and payments methods
    """
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Текст')
    map = models.CharField(max_length=256, blank=True, null=True, verbose_name='Скрипт карты')
    modified_date = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Доставка и оплата'
        verbose_name_plural = 'Доставка и оплата'


class Basket(models.Model):
    """
    Basket model
    """
    client = models.ForeignKey(Clients, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Клиент")
    good_id = models.IntegerField(verbose_name="ID товара")
    good_pn = models.CharField(max_length=128, null=True, blank=True, verbose_name="Артикул")
    good = models.TextField(max_length=128, null=True, blank=True, verbose_name="Товар")
    quantity = models.IntegerField(default=0, verbose_name="Количество")
    meassure = models.CharField(max_length=128, null=True, blank=True, verbose_name="Единица измерения")
    stock_price = models.FloatField(verbose_name="Цена по акции" , default=0.0)
    private_price = models.FloatField(verbose_name="Цена с учетом личной скидки" , default=0.0)
    good_price = models.FloatField(verbose_name="Цена за единицу")
    total_price = models.FloatField(verbose_name="Сумма")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата")

    def __unicode__(self):
        return u'%s' % (self.client.title + ' ' + self.date.strftime('%Y %b %d %H:%M'))

    def __str__(self):
        return "{title} {date}".format(title=self.client.title, date=self.date.strftime('%Y %b %d %H:%M'))

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        ordering = ['-date']


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

# Wait signal of successful payments
result_received.connect(payment_received)
