# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0


import os
import decimal
import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.core.serializers import serialize

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.utils.decorators import method_decorator

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Q

from autoshop.settings import EMAIL_HOST_USER, ALLOWED_HOSTS, MEDIA_ROOT, MEDIA_URL, ROBOKASSA_LOGIN, \
    ROBOKASSA_PASSWORD1, ROBOKASSA_PASSWORD2
from .models import Goods, Clients, Pages, Orders, Contacts, AboutCompany, ForSuppliers, DeliveryInfo, FAQ, \
    Supplier, PriceList, Markup, GoodsCategory, Stock, Developer, Export1C, OrderDetails, Bills, Basket, \
    DeliveryMethods, PaymentsMethods, ClientsPriceCategory
from .forms import ClientRegistrationForm, RestorePasswordForm, UploadPriceListForm, CreateMarkupByPropertyForm, \
    CreateStockForm, EditDeveloperForm, EditCategoryForm, NewExport1CGoodsForm, ChangeClientPasswordEmailForm, \
    ChangeOrderForm, BillsChangeForm, AdmUserChangeForm, AdminCreateForm, ChoosePayDeliveryForm, EnterDeliveryAddress, \
    lkEditClientForm, OrgClientRegistrationForm
from .functions import create_password_str, check_admin_group, raise_403, parse_pricelist, insert_pricelist_data, \
    change_markup, calculate_stock, export_goods_to_excel, delete_order_detail, check_goods_remainder, \
    orders_to_excel, search_goods_func, check_basket_quantity, calculate_basket_total, calculate_basket_summ, \
    check_client_category, add_photo

from number_to_text import decimal2text

from robokassa.forms import RobokassaForm

from watermarker.templatetags.watermark import watermark, Watermarker


# Create your views here

# ----------------Registration and login/logout views ----------------------------------

# ----------- Fixed 17.04.2015 ----------------------------------------
def org_registration_form(request):
    """
    Register new organiozation client form
    """
    if request.user.is_authenticated():
        # Redirect to private office
        return HttpResponseRedirect('/lk/')
    if request.method == 'POST':
        form = OrgClientRegistrationForm(request.POST)
        if form.is_valid():
            # Create user
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    new_user = User.objects.create_user(form.cleaned_data['login'], form.cleaned_data['email'],
                                                    form.cleaned_data['password1'])
                    new_user.save()
                except:
                    errors = u"Произошла ошибка при создании пользователя"
                try:
                    new_client = Clients()
                    # Get user object and add it to a clients group and set it's category to private person
                    user_object = User.objects.get(username=form.cleaned_data['login'])
                    clients_group = Group.objects.get(name="Клиенты")
                    clients_price_group = ClientsPriceCategory.objects.get(title="Частное лицо")
                    password = form.cleaned_data['password1']
                    user_object.groups.add(clients_group)
                    # Create new client object
                    new_client.login = user_object
                    new_client.title = form.cleaned_data['title']
                    new_client.clients_category = clients_price_group
                    new_client.is_org = True
                    new_client.contact_email = form.cleaned_data['email']
                    new_client.contact_phone = form.cleaned_data['phone']
                    new_client.contact_name = form.cleaned_data['contact_name']
                    new_client.law_data = form.cleaned_data['law_data']
                    new_client.law_address = form.cleaned_data['law_address']
                    new_client.save()
                except:
                    errors = u"Произошла ошибка при записи в базу"
                email_subject = u"Регистрация на сайте Sinkai Auto"
                email_message = u"""Здравствуйте! Вы зарегистрировались на сайте %(host)s \n
                    Ваш пароль: %(password)s \n Ваше имя пользователя: %(username)s. \n С уважением, \n
                    Администрация интернет-магазина Синкай Авто""" % {'host': ALLOWED_HOSTS, 'password': password,
                                                                      'username': new_client.login}
                recipients = [user_object.email]
                try:
                    # Try to send email
                    send_mail(email_subject, email_message, EMAIL_HOST_USER, recipients)
                except:
                    errors = u"Возникла непредвиденная ошибка! Попробуйте позднее"
                return HttpResponseRedirect('/regsuccess/')
            else:
                errors = u"Пароль и подтверждение не совпадают. Попробуйте еще раз."
        else:
            errors = u"""Возможно имя пользователя или email заняты или произошла ошибка при заполнении полей.
            Попробуйте еще раз."""
            form = OrgClientRegistrationForm()
            return render_to_response('org_regform.html', {'form': form, 'errors': errors},
                                      context_instance=RequestContext(request))
    else:
        form = OrgClientRegistrationForm()
        return render_to_response('org_regform.html', {'form': form},
                                  context_instance=RequestContext(request))

# ----------- endfix ----------------------------------------

def reg(request):
    """
    Register new client form
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        # Redirect to private office
        return HttpResponseRedirect('/lk/')
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            # Create user
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    new_user = User.objects.create_user(form.cleaned_data['login'], form.cleaned_data['email'],
                                                    form.cleaned_data['password1'])
                    new_user.save()
                except:
                    errors = u"Произошла ошибка при создании пользователя"
                try:
                    new_client = Clients()
                    # Get user object and add it to a clients group and set it's category to private person
                    user_object = User.objects.get(username=form.cleaned_data['login'])
                    clients_group = Group.objects.get(name="Клиенты")
                    clients_price_group = ClientsPriceCategory.objects.get(title="Частное лицо")
                    password = form.cleaned_data['password1']
                    user_object.groups.add(clients_group)
                    # Create new client object
                    new_client.login = user_object
                    new_client.title = form.cleaned_data['title']
                    new_client.clients_category = clients_price_group
                    new_client.is_org = False
                    new_client.contact_email = form.cleaned_data['email']
                    new_client.contact_phone = form.cleaned_data['phone']
                    new_client.save()
                except:
                    errors = u"Произошла ошибка при записи в базу"
                email_subject = u"Регистрация на сайте Sinkai Auto"
                email_message = u"""Здравствуйте! Вы зарегистрировались на сайте %(host)s \n Ваш пароль: %(password)s \n
                Ваше имя пользователя: %(username)s. \n С уважением, \n Администрация интернет-магазина Синкай Авто""" \
                                % {'host': ALLOWED_HOSTS, 'password': password, 'username': new_client.login}
                recipients = [user_object.email]
                try:
                    # Try to send email
                    send_mail(email_subject, email_message, EMAIL_HOST_USER, recipients)
                except:
                    errors = u"Возникла непредвиденная ошибка! Попробуйте позднее"
                return HttpResponseRedirect('/regsuccess/')
            else:
                errors = u"Пароль и подтверждение не совпадают. Попробуйте еще раз."
        else:
            errors = u"Возможно имя пользователя или email заняты. Попробуйте еще раз."
            form = ClientRegistrationForm()
            return render_to_response('regform.html', {'form': form, 'errors': errors},
                                      context_instance=RequestContext(request))
    else:
        form = ClientRegistrationForm()
        return render_to_response('regform.html', {'form': form},
                                  context_instance=RequestContext(request))

def regsuccess(request):
    """
    Success registration view
    """
    return render_to_response('regsuccess.html', context_instance=RequestContext(request))


def login_lk(request):
    """
    Handler for login form in base.html template
    """
    # TODO: change to redirect on main page
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
                    return redirect('mgmt_index')
                else:
                    return redirect('lk')
            else:
                error = u"Ваша учетная запись отключена. Обратитесь к администратору."
        else:
            error = u"Пользователь с таким логином или паролем не найден. Попробуйте еще раз."
        return render_to_response('login_lk_err.html', {'error': error},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def login_page(request):
    """
    Login page view (for redirect by @login_required() decorator.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.POST.get('next', '/lk/'))
        else:
            error = u"Пользователь с таким логином или паролем не найден. Попробуйте еще раз."
            return render_to_response('login_lk_err.html', {'error': error},
                                      context_instance=RequestContext(request))
    next_req = '/lk/'
    if 'next' in request.GET:
        if request.GET['next'] != '':
            next_req = request.GET['next']
    form = AuthenticationForm()
    return render_to_response('login_lk.html', {'form': form, 'next': next_req},
                              context_instance=RequestContext(request))


def restore_password(request):
    """
    Restore password view
    """
    errors = []  # Errors array, for show user what's wrong
    success = False  # If True get user and send email completed successfuly. SHow message in template
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            restore_email = request.POST['email_field']
            try:
                user = User.objects.get(email=restore_email)  # Looking for user with entered email
                temp_password = create_password_str()  # Generate password
                user.set_password(temp_password)
                user.save()
                email_subject = u"Запрос на восстановление пароля Sinkai Auto"
                email_message = u"Здравствуйте! Вы запросили восстановление пароля на сайте %(host)s \n Ваш новый пароль: %(temp_password)s \n Вы можете изменить пароль на сайте в личном кабинете. \n С уважением, \n Администрация интернет-магазина Синкай Авто" % {
                    'host': ALLOWED_HOSTS, 'temp_password': temp_password}
                recipients = [user.email]
                try:
                    # Try to send email
                    send_mail(email_subject, email_message, EMAIL_HOST_USER, recipients)
                    success = True
                except:
                    errors.append(u"Возникла непредвиденная ошибка! Попробуйте позднее")
            except ObjectDoesNotExist:
                errors.append(u"Пользователь с таким адресом не найден.")
        else:
            errors.append(u"Вы ввели неправильный email!")
    form = RestorePasswordForm()
    return render_to_response('restore_password.html', {'errors': errors, 'form': form, 'success': success},
                              context_instance=RequestContext(request))


def logout_lk(request):
    """Logout view."""
    logout(request)
    return redirect('/')


# --------------------Admin panel views----------------------------------------------

@login_required()
def mgmt_index(request):
    """
    Managment (custom admin) view. Show last 15 orders and 15 users.
    """
    # Check that user in group, which has rights
    if check_admin_group(request, "Менеджеры") or check_admin_group(request, "Администраторы"):
        last_clients = Clients.objects.all().order_by('-registration_date')[:15]
        last_orders = Orders.objects.all().order_by('-created_date')[:15]
        return render_to_response('mgmt/index.html', {'last_clients': last_clients, 'last_orders': last_orders},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


@login_required()
def mgmt_index_pages(request):
    """
    Section pages index view.
    """
    if check_admin_group(request, "Администраторы"):
        about_company = AboutCompany.objects.get(pk=1)
        supplier = ForSuppliers.objects.get(pk=1)
        contact = Contacts.objects.get(pk=1)
        delivery = DeliveryInfo.objects.get(pk=1)
        return render_to_response('mgmt/pages_index.html', {'about_company': about_company, 'supplier': supplier,
                                                            'contact': contact, 'delivery': delivery},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


class FAQListView(ListView):
    """
    Return all questions in faq
    """
    template_name = 'mgmt/faq_list.html'
    model = FAQ

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(FAQListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class FAQCreateView(CreateView):
    """
    Create faq question view
    """
    model = FAQ
    template_name = 'mgmt/faq_new.html'
    fields = ['question', 'answer', ]

    def get_success_url(self):
        return reverse('faq-edit-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(FAQCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class FAQUpdateView(UpdateView):
    """
    Create faq question view
    """
    model = FAQ
    template_name = 'mgmt/faq_edit.html'
    fields = ['question', 'answer', 'modified_date']

    def get_success_url(self):
        return reverse('faq-edit-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(FAQUpdateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class FAQDeleteView(DeleteView):
    """
    Delete faq view
    """
    model = FAQ
    template_name = 'mgmt/faq_delete.html'

    def get_success_url(self):
        return reverse('faq-edit-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(FAQDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class AboutCompanyEditView(UpdateView):
    """
    About company edit view
    """
    model = AboutCompany
    template_name = 'mgmt/about_company.html'
    fields = ['title', 'content', 'bank_name', 'inn', 'kpp', 'bik', 'company_name', 'kor_account', 'account',
              'reg_data', 'law_address', 'ceo', 'buh', 'modified_date']

    def get_success_url(self):
        return reverse('aboutcompany-edit', args=[self.object.pk, ])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(AboutCompanyEditView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class ForSuppliersEditView(UpdateView):
    """
    For suppliers edit view
    """
    model = ForSuppliers
    template_name = 'mgmt/for_suppliers.html'
    fields = ['title', 'content', 'modified_date']

    def get_success_url(self):
        return reverse('forsuppliers-edit', args=[self.object.pk, ])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(ForSuppliersEditView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class DeliveryInfoEditView(UpdateView):
    """
    Delivery info edit view
    """
    model = DeliveryInfo
    template_name = 'mgmt/delivery_info.html'
    fields = ['title', 'content', 'map', 'modified_date']

    def get_success_url(self):
        return reverse('deliveryinfo-edit', args=[self.object.pk])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(DeliveryInfoEditView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class ContactsEditView(UpdateView):
    """
    Contact edit view
    """
    model = Contacts
    template_name = 'mgmt/contacts.html'
    fields = ['phone', 'zip', 'address', 'email', 'comments', 'map']

    def get_success_url(self):
        return reverse('contacts-edit', args=[self.object.pk])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(ContactsEditView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PagesListView(ListView):
    """
    Return all created pages
    """
    template_name = 'mgmt/pages_list.html'
    model = Pages

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PagesListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PagesCreateView(CreateView):
    """
    Create page view
    """
    model = Pages
    template_name = 'mgmt/pages_new.html'
    fields = ['title', 'url', 'content', 'image']

    def get_success_url(self):
        return reverse('pages-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PagesCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PagesDetailView(UpdateView):
    """
    Edit page view
    """
    model = Pages
    template_name = 'mgmt/pages_edit.html'
    fields = ['title', 'url', 'content', 'image', 'modified_date']

    def get_success_url(self):
        return reverse('pages-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PagesDetailView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PagesDeleteView(DeleteView):
    """
    Delete page view
    """
    model = Pages
    template_name = 'mgmt/pages_delete.html'

    def get_success_url(self):
        return reverse('pages-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PagesDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def supp_index(request):
    """
    Show index page of suppliers section
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        return render_to_response("mgmt/supp_index.html", context_instance=RequestContext(request))
    else:
        return raise_403(request)


class SupplierCreateView(CreateView):
    """
    Supplier create view
    """
    model = Supplier
    template_name = 'mgmt/supp_new.html'
    fields = ['title', 'bank_data', 'law_address', 'fact_address', 'contact', 'contact_phone', 'contact_email']

    def get_success_url(self):
        return reverse('supp-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(SupplierCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class SupplierListView(ListView):
    """
    Supplier list view
    """
    model = Supplier
    template_name = 'mgmt/supp_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(SupplierListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class SupplierDeleteView(DeleteView):
    """
    Supplier delete view
    """
    model = Supplier
    template_name = 'mgmt/supp_delete.html'

    def get_success_url(self):
        return reverse('supp-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(SupplierDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class SupplierUpdateView(UpdateView):
    """
    Supplier update view
    """
    model = Supplier
    template_name = 'mgmt/supp_edit.html'
    fields = ['title', 'bank_data', 'law_address', 'fact_address', 'contact', 'contact_phone', 'contact_email']

    def get_success_url(self):
        return reverse('supp-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(SupplierUpdateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PriceListListView(ListView):
    """
    List all pricelists view
    """
    model = PriceList
    template_name = 'mgmt/price_list.html'
    paginate_by = 30

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(PriceListListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PriceListDeleteView(DeleteView):
    """
    Delete price list view
    """
    model = PriceList
    template_name = 'mgmt/price_list_delete.html'

    def get_success_url(self):
        return reverse('price-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # For exclude "to many SQL" error delete goods
        # while Goods.objects.filter(price_list=self.object).count():
        #     Goods.objects.filter(price_list=self.object)[0].delete()
        Goods.objects.filter(price_list=self.object).delete()
        # Remove file from disk
        path = self.object.file.path
        try:
            os.remove(path)
        except:
            pass
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(PriceListDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def pricelist_upload(request):
    """Pricelist upload view."""
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        errors = []
        if request.method == 'POST':
            form = UploadPriceListForm(request.POST, request.FILES)
            if form.is_valid():
                new_price = form.save()
                price_ip = ClientsPriceCategory.objects.get(code='ip')
                price_ltd = ClientsPriceCategory.objects.get(code='ltd')
                try:
                    # Read file and get header and first 5 row for preview
                    data = parse_pricelist(new_price.file.path)
                    header = data[0]
                    data_rows = data[1][:5]
                    # Get Goods fields names for create relationship between header in file and models fields
                    goods_model_fields = [Goods._meta.get_field("category").name,
                                          Goods._meta.get_field("developer").name,
                                          Goods._meta.get_field("partnumber").name, Goods._meta.get_field("title").name,
                                          Goods._meta.get_field("description").name,
                                          Goods._meta.get_field("remainder").name,
                                          Goods._meta.get_field("delivery_time").name,
                                          Goods._meta.get_field("cost").name, Goods._meta.get_field("supplier").name]
                    return render_to_response('mgmt/price_list_preview.html', {'pricelist': new_price, 'header': header,
                                                                               'data_rows': data_rows,
                                                                               'instance': Goods,
                                                                               'goods_model_fields': goods_model_fields,
                                                                               'price_ip': price_ip,
                                                                               'price_ltd': price_ltd},
                                              context_instance=RequestContext(request))
                except:
                    errors.append(u"Произошла ошибка при чтении файла")
            else:
                errors.append(u"Произошла ошибка при загрузке файла. Попробуйте снова.")
        form = UploadPriceListForm()
        return render_to_response('mgmt/price_list_new.html', {'errors': errors, 'form': form},
                                  context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def pricelist_to_goods(request):
    """
    Parse xls price list and add Goods model
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        if request.method == 'POST':
            filename = request.POST['file']
            if request.POST['markup'] is not '':
                markup = request.POST['markup']
            else:
                markup = 0
            if request.POST['delivery'] is not '':
                delivery_time = request.POST['delivery']
            else:
                delivery_time = 0
            if request.POST['price_ip'] is not '':
                price_ip = request.POST['price_ip']
            else:
                price_ip = 0
            if request.POST['price_ltd'] is not '':
                price_ltd = request.POST['price_ltd']
            else:
                price_ltd = 0
            # if request.POST['opt'] is not  '':
            #     price_opt = True
            # else:
            #     price_opt = False
            try:
                insert_pricelist_data(filename, delivery_time, markup, price_ip, price_ltd)
                errors = u"Товары были упешно добавлены."
            except:
                errors = u"Произошла ошибка при добавлении товаров."
            return render_to_response('mgmt/price_list_parse.html', {'errors': errors},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


class MarkupListView(ListView):
    """
    Markup list view
    """
    model = Markup
    template_name = 'mgmt/markup_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(MarkupListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def markup_create(request):
    """
    Create markup view.
    :param request:
    :return: HttpResponse
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        if request.method == 'POST':
            form = CreateMarkupByPropertyForm(request.POST)
            if form.is_valid():
                new_markup = form.save()
                if change_markup(form):
                    return redirect('markup-list')
                else:
                    error = u"Произошла ошибка при обновлении наценки."
                    return render_to_response('mgmt/markup_new.html', {'form': form, 'error': error},
                                              context_instance=RequestContext(request))
        form = CreateMarkupByPropertyForm()
        return render_to_response('mgmt/markup_new.html', {'form': form},
                                  context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def markup_edit(request, pk):
    """
    Edit markup view
    :param request: Request object
    :param pk: id of markup
    :return: return HttpResponse
    """
    error = ''
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        markup = get_object_or_404(Markup, pk=pk)
        if request.method == 'POST':
            form = CreateMarkupByPropertyForm(request.POST, instance=markup)
            if form.is_valid():
                new_markup = form.save()
                if change_markup(form):
                    return redirect('markup-list')
                else:
                    error = u"Произошла ошибка при обновлении наценки."
                    return render_to_response('mgmt/markup_edit.html', {'form': form, 'error': error},
                                              context_instance=RequestContext(request))
        else:
            form = CreateMarkupByPropertyForm(instance=markup)
            return render_to_response('mgmt/markup_edit.html', {'form': form, 'error': error},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


class MarkupDeleteView(DeleteView):
    """
    Markup delete view
    """
    model = Markup
    template_name = 'mgmt/markup_delete.html'

    def get_success_url(self):
        return reverse('markup-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(MarkupDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class StockListView(ListView):
    """
    Stock list view
    """
    model = Stock
    template_name = 'mgmt/stock_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(StockListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def create_stock(request):
    """
    Create stock view.
    :param request: Request object
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        error = ''
        if request.method == 'POST':
            form = CreateStockForm(request.POST)
            if form.is_valid():
                new_stock = form.save()
                if calculate_stock(new_stock):
                    return redirect('stock-list')
                else:
                    error = u"Произошла ошибка при создании акции! Обратитесь а администратору."
            else:
                error = u"Произошла ошибка! Проверьте правильность введеных данных или обратитесь а администратору."
        form = CreateStockForm()
        return render_to_response('mgmt/stock_new.html', {'form': form, 'error': error},
                                  context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def edit_stock(request, pk):
    """
    Edit stock view
    :param request: request object
    :param pk: stock id
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        error = ''
        stock = get_object_or_404(Stock, pk=pk)
        if request.method == 'POST':
            form = CreateStockForm(request.POST, instance=stock)
            if form.is_valid():
                new_stock = form.save()
                if calculate_stock(new_stock):
                    return redirect('stock-list')
                else:
                    error = u"Произошла ошибка при обновлении акции! Обратитесь а администратору."
                    return render_to_response('mgmt/stock_edit.html', {'form': form, 'error': error},
                                              context_instance=RequestContext(request))
        else:
            form = CreateStockForm(instance=stock)
            return render_to_response('mgmt/stock_edit.html', {'form': form, 'error': error},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


class DeleteStockView(DeleteView):
    """
    Delete stock view. Change stock price for goods to 0.
    """
    model = Stock
    template_name = 'mgmt/stock_delete.html'

    def get_success_url(self):
        return reverse('stock-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        goods = Goods.objects.filter(stock=self.object)
        for good in goods:
            good.stock_price = 0
            good.save()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(DeleteStockView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class GoodsListView(ListView):
    """
    Goods list view
    """
    model = Goods
    template_name = 'mgmt/goods_list.html'
    paginate_by = 100

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(GoodsListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def goods_mgmt_search(request):
    """
    Search goods in admin panel
    :param request: request object
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        if 'word' in request.POST:
            word = request.POST['word']
            objects = search_goods_func(word, True)
            paginator = Paginator(objects, 100)
            page = request.GET.get('page')
            try:
                object_list = paginator.page(page)
            except PageNotAnInteger:
                object_list = paginator.page(1)
            except EmptyPage:
                object_list = paginator.page(paginator.num_pages)
            return render_to_response("mgmt/goods_search.html", {'object_list': object_list},
                                      context_instance=RequestContext(request))
        if 'page' in request.GET:
            word = request.session['search']  # get searching word from session variable
            objects = search_goods_func(word, True)
            request.session['search'] = word
            paginator = Paginator(objects, 100)
            page = request.GET.get('page')
            try:
                object_list = paginator.page(page)
            except PageNotAnInteger:
                object_list = paginator.page(1)
            except EmptyPage:
                object_list = paginator.page(paginator.num_pages)
            return render_to_response("mgmt/goods_search.html", {'object_list': object_list},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


class GoodsCreateView(CreateView):
    """
    Create goods view.
    """
    model = Goods
    template_name = 'mgmt/goods_new.html'
    fields = ['category', 'developer', 'partnumber', 'title', 'description', 'show_on_index',
              'remainder', 'reserved', 'delivery_time', 'meassure', 'price', 'cost', 'supplier', 'stock_price']

    def get_success_url(self):
        return reverse('goods-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(GoodsCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class GoodsUpdateView(UpdateView):
    """
    Edit goods view.
    """
    model = Goods
    template_name = 'mgmt/goods_edit.html'
    fields = ['category', 'developer', 'partnumber', 'internal_partnumber', 'title', 'description', 'show_on_index',
              'remainder', 'reserved', 'delivery_time', 'meassure', 'price', 'price_ip', 'price_org',
              'cost', 'stock_price']

    def get_success_url(self):
        return reverse('goods-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(GoodsUpdateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class GoodsDeleteView(DeleteView):
    """
    Delete goods view.
    """
    model = Goods
    template_name = 'mgmt/goods_delete.html'

    def get_success_url(self):
        return reverse('goods-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(GoodsDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def dev_cat_list(request):
    """
    Show lists developers and categories
    :param request:
    :return: HttpResponse
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        developers = Developer.objects.all()
        categories = GoodsCategory.objects.all()
        return render_to_response('mgmt/goods-dev-cat.html', {'developers': developers, 'categories': categories},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


class DeveloperCreateView(CreateView):
    """
    Create developer view.
    """
    model = Developer
    template_name = 'mgmt/dev_new.html'
    fields = ['title']

    def get_success_url(self):
        return reverse('goods-dev-cat')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(DeveloperCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def edit_developer(request, pk):
    """
    Edit developer view
    :param request: request object
    :param pk: id of developer
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        developer = get_object_or_404(Developer, pk=pk)
        error = ''
        if request.method == 'POST':
            form = EditDeveloperForm(request.POST, instance=developer)
            if form.is_valid():
                dev = form.save()
                return redirect('goods-dev-cat')
            else:
                error = u"Произошла ошибка. Попробуйте снова или обратитесь к администратору."
        form = EditDeveloperForm(instance=developer)
        goods = Goods.objects.filter(developer=developer)
        return render_to_response('mgmt/dev_edit.html', {'error': error, 'form': form, 'object': developer,
                                                         'goods': goods},
                                  context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def add_goods_to_developer(request):
    """
    Show search results for add goods.
    :param request: request object.
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        error = ''
        if request.method == 'POST':
            # Check if it was search for goods to add
            if 'word' in request.POST:
                word = request.POST['word']
                dev_id = request.POST['id_developer']
                developer = Developer.objects.get(pk=dev_id)
                goods = search_goods_func(word, True)
                return render_to_response('mgmt/dev_add_goods.html', {'object': developer, 'goods': goods},
                                          context_instance=RequestContext(request))
            # check if it was add goods to developer
            elif 'goods' in request.POST:
                add_goods = request.POST.getlist('goods')
                id_developer = request.POST['object_id']
                developer = Developer.objects.get(pk=id_developer)
                for good_id in add_goods:
                    good = Goods.objects.get(pk=good_id)
                    good.developer = developer
                    good.save()
                return redirect('goods-dev-cat')
            else:
                error = u"Неправильные параметры запроса."
        else:
            error = u"Неправильный метод запроса."
            return render_to_response('mgmt/error_page.html', {'error': error},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def delete_dev_goods(request, pk):
    """
    Set good's developer to None
    :param request: request object
    :param pk: id of good
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        good = get_object_or_404(Goods, pk=pk)
        good.developer = None
        good.save()
        return redirect('goods-dev-cat')
    else:
        raise_403(request)


class DeveloperDeleteView(DeleteView):
    """
    Developer delete view
    """
    model = Developer
    template_name = 'mgmt/dev_delete.html'

    def get_success_url(self):
        return reverse('goods-dev-cat')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(DeveloperDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class CategoryCreateView(CreateView):
    """
    Create category view.
    """
    model = GoodsCategory
    template_name = 'mgmt/cat_new.html'
    fields = ['title']

    def get_success_url(self):
        return reverse('goods-dev-cat')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(CategoryCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def edit_category(request, pk):
    """
    Edit category view
    :param request: request object
    :param pk: id of category
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        category = get_object_or_404(GoodsCategory, pk=pk)
        error = ''
        if request.method == 'POST':
            form = EditCategoryForm(request.POST, instance=category)
            if form.is_valid():
                dev = form.save()
                return redirect('goods-dev-cat')
            else:
                error = u"Произошла ошибка. Попробуйте снова или обратитесь к администратору."
        form = EditCategoryForm(instance=category)
        goods = Goods.objects.filter(category=category)
        return render_to_response('mgmt/cat_edit.html', {'error': error, 'form': form, 'object': category,
                                                         'goods': goods},
                                  context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def add_goods_to_category(request):
    """
    Show search results for add goods.
    :param request: request object.
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        error = ''
        if request.method == 'POST':
            # Check if it was search for goods to add
            if 'word' in request.POST:
                word = request.POST['word']
                cat_id = request.POST['id_category']
                category = GoodsCategory.objects.get(pk=cat_id)
                goods = search_goods_func(word, True)
                return render_to_response('mgmt/cat_add_goods.html', {'object': category, 'goods': goods},
                                          context_instance=RequestContext(request))
            # check if it was add goods to category
            elif 'goods' in request.POST:
                add_goods = request.POST.getlist('goods')
                id_cat = request.POST['object_id']
                category = GoodsCategory.objects.get(pk=id_cat)
                for good_id in add_goods:
                    good = Goods.objects.get(pk=good_id)
                    good.category = category
                    good.save()
                return redirect('goods-dev-cat')
            else:
                error = u"Неправильные параметры запроса."
        else:
            error = u"Неправильный метод запроса."
            return render_to_response('mgmt/error_page.html', {'error': error},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


@login_required()
def delete_cat_goods(request, pk):
    """
    Set good's category to None
    :param request: request object
    :param pk: id of good
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        good = get_object_or_404(Goods, pk=pk)
        good.category = None
        good.save()
        return redirect('goods-dev-cat')
    else:
        raise_403(request)


class CategoryDeleteView(DeleteView):
    """
    Category delete view
    """
    model = GoodsCategory
    template_name = 'mgmt/dev_delete.html'

    def get_success_url(self):
        return reverse('goods-dev-cat')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(CategoryDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class ExportGoodsListView(ListView):
    """
    Export goods list view
    """
    model = Export1C
    queryset = Export1C.objects.filter(type=0)  # get only exports where type = goods (0)
    template_name = 'mgmt/export1c_goods.html'
    paginate_by = 30

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(ExportGoodsListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def create_new_export_goods(request):
    """
    Create new export goods file and export data to it
    :param request:
    :return:
    """
    error = ''
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        if request.method == 'POST':
            form = NewExport1CGoodsForm(request.POST)
            if form.is_valid():
                # Forming file path to save file
                file_name = request.POST['title'] + '.xlsx'
                file_path = MEDIA_ROOT + '/1C/' + file_name
                # Save form
                new_export = form.save()
                # Save filepath to new object
                new_export.file = file_path
                new_export.url = MEDIA_URL + '1C/' + file_name
                new_export.save()
                # Export goods_to_excel
                if export_goods_to_excel(file_path):
                    return redirect('export-goods-list')
                else:
                    error = u"Произошла ошибка во время выгрузки. Обрпатитесь к администратору."
            else:
                error = u"Произошла ошибка. Обратитесь к администратору."
        form = NewExport1CGoodsForm()
        return render_to_response('mgmt/export1c_goods_new.html', {'form': form, 'error': error},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


class Export1CDeleteView(DeleteView):
    """
    Delete export1c view
    """
    model = Export1C
    template_name = 'mgmt/export1c_goods_delete.html'

    def get_success_url(self):
        return reverse('export-goods-list')

    def get_success_url_orders(self):
        return reverse('export-orders-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Remove file from disk
        path = self.object.file
        try:
            os.remove(path)
        except:
            pass
        if self.object.type == 0:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url_orders())


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(Export1CDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def order_index(request):
    """
    Show index of orders section
    :param request:
    :return: HttpResponse
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        return render_to_response('mgmt/order_index.html', context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


class ClientsListView(ListView):
    """
    Clients list view
    """
    model = Clients
    template_name = 'mgmt/clients_list.html'
    paginate_by = 50

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(ClientsListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def clients_search(request):
    """
    Search clients
    :param request: request object
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        if 'word' in request.POST:
            word = request.POST['word']
            objects = Clients.objects.filter(
                Q(title__contains=word) | Q(contact_name__contains=word) | Q(contact_email__contains=word) | Q(
                    contact_phone__contains=word))
            request.session['search_clients'] = word  # save searching word in session variable
            paginator = Paginator(objects, 50)
            page = request.GET.get('page')
            try:
                object_list = paginator.page(page)
            except PageNotAnInteger:
                object_list = paginator.page(1)
            except EmptyPage:
                object_list = paginator.page(paginator.num_pages)
            return render_to_response("mgmt/clients_search.html", {'object_list': object_list},
                                      context_instance=RequestContext(request))
        if 'page' in request.GET:
            word = request.session['search_clients']  # get searching word from session variable
            objects = Clients.objects.filter(
                Q(title__contains=word) | Q(contact_name__contains=word) | Q(contact_email__contains=word) |
                Q(login__contains=word) | Q(contact_phone__contains=word))
            request.session['search_clients'] = word
            paginator = Paginator(objects, 50)
            page = request.GET.get('page')
            try:
                object_list = paginator.page(page)
            except PageNotAnInteger:
                object_list = paginator.page(1)
            except EmptyPage:
                object_list = paginator.page(paginator.num_pages)
            return render_to_response("mgmt/clients_search.html", {'object_list': object_list},
                                      context_instance=RequestContext(request))
    else:
        raise_403(request)


class EditClientView(UpdateView):
    """
    Edit client view
    """
    model = Clients
    template_name = 'mgmt/clients_edit.html'
    fields = ['title', 'contact_name', 'contact_address', 'contact_phone', 'contact_email', 'delivery_zip',
              'delivery_city', 'delivery_street', 'delivery_home', 'delivery_office', 'preferred_payments', 'law_data',
              'law_address', 'private_stock', 'clients_category']

    def get_success_url(self):
        return reverse('clients-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(EditClientView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def change_client_password(request, pk):
    """
    Change client password
    :param request: request object
    :param pk: id of client
    :return:
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        client = get_object_or_404(Clients, pk=pk)
        user = User.objects.get(username=client.login.username)
        error = ''
        if request.method == 'POST':
            form = ChangeClientPasswordEmailForm(request.POST)
            if form.is_valid():
                if request.POST['password1'] != '':
                    pass1 = form.cleaned_data['password1']
                    pass2 = form.cleaned_data['password2']
                    if pass1 == pass2:
                        user.set_password(pass1)
                        user.save()
                    else:
                        error = u"Пароли не совпадают. Попробуйте еще раз."
                elif request.POST['email'] != '':
                    email = form.cleaned_data['email']
                    user.email = email
                    user.save()
                return redirect('clients-list')
            else:
                error = u"Ошибка при заполнении формы. Попробуйте еще раз."
        form = ChangeClientPasswordEmailForm(initial={'email': user.email})
        return render_to_response('mgmt/clients_pass.html', {'form': form, 'error': error,
                                                             'client': client, 'user': user},
                                  context_instance=RequestContext(request))
    else:
        return raise_403(request)


class ClientDeleteView(DeleteView):
    """
    Delete client view
    """
    model = Clients
    template_name = 'mgmt/clients_delete.html'

    def get_success_url(self):
        return reverse('clients-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Remove user
        user = User.objects.get(username=self.object.login.username)
        user.delete()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(ClientDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class OrdersListView(ListView):
    """
    List view orders
    """
    model = Orders
    template_name = 'mgmt/orders_list.html'
    paginate_by = 50

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(OrdersListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def edit_order(request, pk):
    """
    Edit order view
    :param request: request object
    :param pk: pk of order
    :return: HttpResponse
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        order = get_object_or_404(Orders, pk=pk)
        order_details = OrderDetails.objects.filter(order=order)
        error = ''
        if request.method == 'POST':
            if 'order' in request.POST:
                if request.POST['order'] != '':
                    if 'payment_status' in request.POST:
                            if request.POST['payment_status'] == 'on':
                                if order.payment_status == False:
                                    client = Clients.objects.get(login=order.client.login)
                                    client.unpaid_sum -= order.order_sum
                                    client.unpaid_orders -= 1
                                    client.orders_sum += order.order_sum
                                    client.save()
                    form = ChangeOrderForm(request.POST, instance=order)
                    if form.is_valid():
                        form.save()
                        if order.payment_status == True:
                            mess_pay = u"Оплачен"
                        else:
                            mess_pay = u"Не оплачен"
                        mess_status = order.get_status_display()
                        email_subject = u"Изменение вашего заказа в интернет-магазине Синкай-авто"
                        email_message = u"Ваш заказ " + str(order) + u" изменился. \n Статус оплаты вашего заказа: " + mess_pay + u" \n Статус вашего заказа: " + mess_status + u" \n С уважением, \n Администрация магазина Синкай-Авто"
                        email_message2 = u"Заказ " + str(order) + u" изменился. \n Статус оплаты заказа: " + mess_pay + u" \n Статус заказа: " + mess_status + u" \n С уважением, \n Администрация магазина Синкай-Авто"
                        recipients = [order.client.contact_email]
                        try:
                            # Try to send email
                            send_mail(email_subject, email_message, EMAIL_HOST_USER, recipients)
                        except:
                            error = u"Не удалось отправить оповещение клиенту"
                        admins = User.objects.filter(Q(groups__name="Менеджеры") | Q(groups__name="Администраторы") |
                                     Q(is_superuser=True))
                        recipients2 = []
                        for adm in admins:
                            recipients2.append(adm.email)
                        try:
                            # Try to send email
                            send_mail(email_subject, email_message2, EMAIL_HOST_USER, recipients2)
                        except:
                            error = u"Не удалось отправить оповещение администраторам"
                        if request.POST['status'] in ('2', '3', '4', '5'):
                            for details in order_details:
                                try:
                                    reserved_good = Goods.objects.get(pk=details.goods_id)
                                except:
                                    reserved_good = Goods.objects.get(partnumber=details.goods_pn)
                                reserved_good.reserved = reserved_good.reserved - details.quantity
                                reserved_good.save()
                    else:
                        client = Clients.objects.get(title=order.client.title)
                        client.unpaid_sum += order.order_sum
                        client.unpaid_orders += 1
                        client.orders_sum -= order.order_sum
                        client.save()
                        error = u"Ошибка при изменении свойств заказа."
            elif 'id_order' in request.POST:
                if request.POST['id_order'] != '':
                    # Add good to order
                    goods = Goods.objects.filter(Q(partnumber__contains=request.POST['partnumber']) | Q(
                        title__contains=request.POST['partnumber']))
                    return render_to_response('mgmt/order_add_goods.html', {'order': order, 'goods': goods},
                                              context_instance=RequestContext(request))
                else:
                    error = u"Произошла ошибка при добавлении товара"
            elif 'order_detail' in request.POST:
                # change quantity of goods in orders detail
                if request.POST['order_detail'] != '':
                    order_detail = OrderDetails.objects.get(pk=request.POST['order_detail'])
                    if request.POST['quantity'] == '0':
                        delete_order_detail(order_detail, order)
                    else:
                        try:
                            good_in_order = Goods.objects.get(pk=order_detail.goods_id)
                        except ObjectDoesNotExist:
                            good_in_order = Goods.objects.get(partnumber=order_detail.goods_pn)
                        if not check_goods_remainder(good_in_order):
                            error = u"Ошибка. Запрошенного товара нет на складе."
                            return render_to_response('mgmt/error_page.html', {'error': error},
                                                      context_instance=RequestContext(request))
                        good_in_order.remainder += order_detail.quantity
                        good_in_order.reserved -= order_detail.quantity
                        good_in_order.remainder -= int(request.POST['quantity'])
                        good_in_order.reserved += int(request.POST['quantity'])
                        order_detail.quantity = int(request.POST['quantity'])
                        order_detail.total_goods_price = round((order_detail.goods_price * order_detail.quantity), 2)
                        order_detail.save()
                        good_in_order.save()
                        orders_details = OrderDetails.objects.filter(order=order)
                        order.order_sum = 0
                        for det in orders_details:
                            order.order_sum = round((order.order_sum + det.total_goods_price), 2)
                        order.save()
                else:
                    error = u"Произошла ошибка при изменении количества товаров."
            elif 'delete_detail' in request.POST:
                # Delete goods from order
                if request.POST['delete_detail'] != '':
                    order_detail_delete = OrderDetails.objects.get(pk=request.POST['delete_detail'])
                    delete_order_detail(order_detail_delete, order)
                else:
                    error = u"Произошла ошибка при удалении товара."
        form = ChangeOrderForm(instance=order)
        return render_to_response('mgmt/orders_edit.html', {'form': form, 'order': order, 'error': error,
                                                            'order_details': order_details},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


@login_required()
def add_goods_to_order(request):
    """
    Add goods to order view
    :param request: request object
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        error = ''
        if request.method == 'POST':
            if 'goods' in request.POST:
                list_goods = request.POST.getlist('goods')
                order_id = request.POST['order_id']
                order = Orders.objects.get(pk=order_id)
                for good_id in list_goods:
                    good = Goods.objects.get(pk=good_id)
                    new_order_detail = OrderDetails()
                    new_order_detail.order = order
                    new_order_detail.goods_id = good.pk
                    new_order_detail.goods = good.title
                    new_order_detail.goods_pn = good.partnumber
                    new_order_detail.meassure = good.meassure
                    new_order_detail.quantity = 1
                    # If good in stock get stock price
                    if good.stock_price == 0:
                        new_order_detail.goods_price = good.price
                        new_order_detail.total_goods_price = good.price
                    else:
                        new_order_detail.goods_price = good.stock_price
                        new_order_detail.total_goods_price = good.stock_price
                    # Increment number of reserved goods
                    if not check_goods_remainder(good):
                        error = u"Ошибка. Запрошенного товара нет на складе."
                        return render_to_response('mgmt/error_page.html', {'error': error},
                                                  context_instance=RequestContext(request))
                    good.remainder = good.remainder - 1
                    good.reserved = good.reserved + 1
                    good.save()
                    new_order_detail.save()
                    order.order_sum = round((order.order_sum + new_order_detail.total_goods_price), 2)
                    order.save()
                return redirect('orders-edit', order.pk)
            else:
                error = u"Не выбран не один товар."
                return render_to_response('mgmt/error_page.html', {'error': error},
                                          context_instance=RequestContext(request))
        else:
            error = u"Ошибка запроса."
            return render_to_response('mgmt/error_page.html', {'error': error},
                                      context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


class DeleteOrderView(DeleteView):
    """
    Delete order view
    """
    model = Orders
    template_name = 'mgmt/order_delete.html'

    def get_success_url(self):
        return reverse('orders-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Set all reserve and remainders
        orders_details = OrderDetails.objects.filter(order=self.object)
        if not self.object.payment_status:
            if self.object.client.unpaid_sum >= self.object.order_sum:
                self.object.client.unpaid_sum -= self.object.order_sum
            if self.object.client.unpaid_orders > 0:
                self.object.client.unpaid_orders -= 1
        self.object.client.save()
        for detail in orders_details:
            delete_order_detail(detail, self.object)
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(DeleteOrderView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class BillsListView(ListView):
    """
    List view bills
    """
    model = Bills
    template_name = 'mgmt/bills_list.html'
    paginate_by = 50

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(BillsListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def change_bill(request, pk):
    """
    Change bill view. Show bill for print.
    :param request: request object
    :param pk: id og the bill
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        error = ''
        bill = get_object_or_404(Bills, pk=pk)
        if request.method == 'POST':
            form = BillsChangeForm(request.POST, instance=bill)
            if form.is_valid():
                changed_bill = form.save()
                if changed_bill.bill_status:
                    order = Orders.objects.get(pk=changed_bill.order.pk)
                    if order.payment_status == False and order.payments == 3:
                        client = Clients.objects.get(title=bill.client.title)
                        client.orders_sum = round((client.orders_sum + order.order_sum), 2)
                        client.unpaid_sum = round((client.orders_sum - order.order_sum), 2)
                        client.unpaid_orders -= 1
                        client.save()
                        order.payment_status = True
                        order.save()
                return redirect('bills-list')
            else:
                error = u"Произошла ошибка при изменении счета"
        form = BillsChangeForm(instance=bill)
        return render_to_response('mgmt/bill_edit.html', {'form': form, 'error': error, 'bill': bill},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


@login_required()
def show_bill(request, pk):
    """
    Show bill blank for print.
    :param request: request object
    :param pk: id of bill
    :return: HttpResponse object
    """
    bill = Bills.objects.get(pk=pk)
    company_info = AboutCompany.objects.get(pk=1)
    client = Clients.objects.get(title=bill.client.title)
    order = Orders.objects.get(pk=bill.order.pk)
    orders_details = OrderDetails.objects.filter(order=bill.order)
    nds = round((float(order.order_sum) * 0.18), 2)
    int_units = ((u'рубль', u'рубля', u'рублей'), 'm')
    exp_units = ((u'копейка', u'копейки', u'копеек'), 'f')
    summ_text = decimal2text(decimal.Decimal(order.order_sum), int_units=int_units, exp_units=exp_units)
    return render_to_response('mgmt/bill_blank.html', {'company_info': company_info, 'bill': bill,
                                                       'client': client, 'orders_details': orders_details, 'nds': nds,
                                                       'order': order, 'summ_text': summ_text},
                              context_instance=RequestContext(request))


class DeleteBillView(DeleteView):
    """
    Delete bill view.
    Not used in this version.
    """
    model = Bills
    template_name = 'mgmt/bill_delete.html'

    def get_success_url(self):
        return reverse('bills-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(DeleteBillView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class ExportOrderListView(ListView):
    """
    Export order list view
    """
    model = Export1C
    queryset = Export1C.objects.filter(type=1)  # get only exports where type = orders (1)
    template_name = 'mgmt/export1c_orders.html'
    paginate_by = 30

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы") or check_admin_group(self.request, "Менеджеры"):
            return super(ExportOrderListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def create_new_export_orders(request):
    """
    Create new export ordres file
    :param request: request object
    :return: HttpResponse
    """
    error = ''
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        if request.method == 'POST':
            form = NewExport1CGoodsForm(request.POST)
            if form.is_valid():
                # Forming file path to save file
                file_name = request.POST['title'] + '.xlsx'
                file_path = MEDIA_ROOT + '/1C/' + file_name
                # Save form
                new_export = form.save()
                # Save filepath to new object
                new_export.file = file_path
                new_export.url = MEDIA_URL + '1C/' + file_name
                new_export.type = 1
                new_export.save()
                if orders_to_excel(file_path):
                    return redirect('export-orders-list')
                else:
                    error = u"Произошла ошибка во время выгрузки. Обрпатитесь к администратору."
            else:
                error = u"Произошла ошибка. Обратитесь к администратору."
        form = NewExport1CGoodsForm()
        return render_to_response('mgmt/export1c_goods_new.html', {'form': form, 'error': error},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


@login_required()
def user_list(request):
    """
    Show administrative users list
    :param request: request object
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы"):
        users = User.objects.filter(Q(groups__name="Менеджеры") | Q(groups__name="Администраторы")
                                    | Q(is_superuser=True)).order_by('-last_login')
        return render_to_response("mgmt/admin_user.html", {'users': users},
                                  context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


@login_required()
def change_adm_user(request, pk):
    """
    Change administrators or managers properties
    :param request: request object
    :param pk: id of user
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы"):
        user = User.objects.get(pk=pk)
        error = ''
        if request.method == 'POST':
            form = AdmUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                user.groups = ''
                user.groups.add(Group.objects.get(pk=request.POST['group']))
                user.save()
                return redirect('user-list')
            else:
                error = u"Ошибка при заполнении формы. Попробуйте еще раз."
        form = AdmUserChangeForm(instance=user)
        return render_to_response('mgmt/admin_pass.html', {'form': form, 'error': error, 'user': user},
                                  context_instance=RequestContext(request))
    else:
        return raise_403(request)


@login_required()
def change_admin_password(request, pk):
    """
    Change administrator or manager password
    :param request: request object
    :param pk: id of admin
    :return: HttpResponse object
    """
    if check_admin_group(request, "Администраторы"):
        user = User.objects.get(pk=pk)
        error = ''
        if request.method == 'POST':
            form = ChangeClientPasswordEmailForm(request.POST)
            if form.is_valid():
                if request.POST['password1'] != '':
                    pass1 = form.cleaned_data['password1']
                    pass2 = form.cleaned_data['password2']
                    if pass1 == pass2:
                        user.set_password(pass1)
                        user.save()
                    else:
                        error = u"Пароли не совпадают. Попробуйте еще раз."
                return redirect('user-list')
            else:
                error = u"Ошибка при заполнении формы. Попробуйте еще раз."
        form = ChangeClientPasswordEmailForm()
        return render_to_response('mgmt/admin_pass_change.html', {'form': form, 'error': error, 'user': user},
                                  context_instance=RequestContext(request))
    else:
        return raise_403(request)


class DeleteUserView(DeleteView):
    """
    Delete user view.
    """
    model = User
    template_name = 'mgmt/admin_delete.html'

    def get_success_url(self):
        return reverse('user-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(DeleteUserView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def admin_add(request):
    """
    Add new administrator view
    """
    if check_admin_group(request, "Администраторы"):
        if request.method == 'POST':
            form = AdminCreateForm(request.POST)
            if form.is_valid():
                # Create user
                new_user = form.save()
                new_user.groups.add(Group.objects.get(pk=request.POST['group']))
                new_user.save()
                return redirect('user-list')
            else:
                errors = u"Возможно имя пользователя или email заняты или не правильно заполнено поле ввода пароля или email. Попробуйте еще раз."
                form = AdminCreateForm()
                return render_to_response('mgmt/admin_add.html', {'form': form, 'errors': errors},
                                          context_instance=RequestContext(request))
        else:
            form = AdminCreateForm()
            return render_to_response('mgmt/admin_add.html', {'form': form},
                                      context_instance=RequestContext(request))
    else:
        # Return access denied
        return raise_403(request)


class DeliveryListView(ListView):
    """
    Delivery methods list view
    """
    model = DeliveryMethods
    template_name = 'mgmt/delivery_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(DeliveryListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class DeliveryMethodCreateView(CreateView):
    """
    Create delivery method.
    """
    model = DeliveryMethods
    template_name = 'mgmt/delivery_new.html'
    fields = ['title', 'description', 'cost']

    def get_success_url(self):
        return reverse('delivery-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(DeliveryMethodCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class DeliveryMethodsUpdateView(UpdateView):
    """
    Edit delivery methods view
    """
    model = DeliveryMethods
    template_name = 'mgmt/delivery_edit.html'
    fields = ['title', 'description', 'cost']

    def get_success_url(self):
        return reverse('delivery-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(DeliveryMethodsUpdateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class DeliveryMethodDeleteView(DeleteView):
    """
    Delete user view.
    """
    model = DeliveryMethods
    template_name = 'mgmt/delivery_delete.html'

    def get_success_url(self):
        return reverse('delivery-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(DeliveryMethodDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PaymentMethodsListView(ListView):
    """
    Payments methods list view
    """
    model = PaymentsMethods
    template_name = 'mgmt/payments_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PaymentMethodsListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PaymentMethodCreateView(CreateView):
    """
    Create payment method.
    """
    model = PaymentsMethods
    template_name = 'mgmt/payments_new.html'
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('payments-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PaymentMethodCreateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PaymentsMethodsUpdateView(UpdateView):
    """
    Edit delivery methods view
    """
    model = PaymentsMethods
    template_name = 'mgmt/payments_edit.html'
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('payments-list')

    @method_decorator(login_required)  # Check that user manager/admin or superuser and logged in
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PaymentsMethodsUpdateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class PaymentMethodDeleteView(DeleteView):
    """
    Delete payment method view.
    """
    model = PaymentsMethods
    template_name = 'mgmt/payments_delete.html'

    def get_success_url(self):
        return reverse('payments-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(PaymentMethodDeleteView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)

class CategoryPriceClientsListView(ListView):
    """
    ClientsPriceCategory list view
    """
    model = ClientsPriceCategory
    template_name = 'mgmt/clients_price_cat.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(CategoryPriceClientsListView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


class ClientsPriceCategoryUpdateView(UpdateView):
    """
    ClientsPriceCategory update view
    """
    model = ClientsPriceCategory
    template_name = 'mgmt/clients_price_cat_edit.html'

    def get_success_url(self):
        return reverse('client-price-cat')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if check_admin_group(self.request, "Администраторы"):
            return super(ClientsPriceCategoryUpdateView, self).dispatch(*args, **kwargs)
        else:
            # Return access denied
            return raise_403(self.request)


@login_required()
def load_photos(request):
    """
    Call function add photo to add image to good.image
    :param request: request object
    :return: HttpResponse to redirect on previous page
    """
    if add_photo():
        error = u"Фотографии были успешно загружены."
        return render_to_response('mgmt/photos_uploaded.html', {'error': error}, context_instance=RequestContext(request))
    else:
        error = u"Ошибка при загрузки фотографий"
        return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))

# ----------------------Shop views ----------------------------------------

def index(request):
    """
    Index page view
    """
    popular_goods = Goods.objects.filter(show_on_index=True)
    stock_goods = Goods.objects.filter(stock__show_on_main_page=True)[:3]
    client_category = check_client_category(request)
    return render_to_response('index.html', {'popular_goods': popular_goods,
                                             'stock_goods': stock_goods,
                                             'client_category': client_category},
                              context_instance=RequestContext(request))


def search_goods(request):
    """
    Search goods in shop view
    :param request: request object
    :return: HttpResponse object
    """
    client_category = check_client_category(request)
    if client_category == None or client_category.code == "pv":
        price_opt = False
    else:
        price_opt = True
    if 'search' in request.GET:
        word = request.GET['search']
        objects = search_goods_func(word, price_opt)
        request.session['search_word'] = word  # save searching word in session variable
        paginator = Paginator(objects, 100)
        page = request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        return render_to_response("search.html", {'object_list': object_list, 'client_category': client_category},
                                  context_instance=RequestContext(request))
    if 'page' in request.GET:
        word = request.session['search_word']  # get searching word from session variable
        objects = search_goods_func(word, price_opt)
        request.session['search_word'] = word
        paginator = Paginator(objects, 100)
        page = request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        return render_to_response("search.html", {'object_list': object_list, 'client_category': client_category},
                                  context_instance=RequestContext(request))


@login_required()
def basket_actions(request):
    """
    Show basket and add/substitute/delete goods in them
    :param request: request object
    :return: Httpresponse object
    """
    error = ""
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        return redirect('mgmt_index')
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
    client_category = check_client_category(request)
    if request.method == 'POST':
        if 'good_id' in request.POST:
            # Add goods to basket
            try:
                client_category = check_client_category(request)
                good = Goods.objects.get(pk=request.POST['good_id'])
                basket = Basket()
                basket.client = client
                basket.good_id = good.pk
                basket.good_pn = good.partnumber
                basket.good = good.title
                basket.quantity = 1
                error = check_basket_quantity(good, basket)
                basket.meassure = good.meassure
                if client_category is not None:
                    if client_category.code == "ip":
                        basket.good_price = good.price_ip
                    elif client_category.code == "ltd":
                        basket.good_price = good.price_org
                    else:
                        basket.good_price = good.price
                        if good.stock_price != 0:
                            basket.stock_price = good.stock_price
                else:
                    basket.good_price = good.price
                    if good.stock_price != 0:
                        basket.stock_price = good.stock_price
                basket.total_price = calculate_basket_total(good, basket)
                basket.save()
            except ObjectDoesNotExist:
                error = u"""Произошла ошибка при добавлении товара. Возможно товар был удален из базы.
                Обратитесь к администратору или попробуйте заново."""
        elif 'delete_id' in request.POST:
            # Delete goods from basket
            basket = Basket.objects.get(pk=request.POST['delete_id'])
            basket.delete()
        elif 'add_id' in request.POST:
            # Add quantity of goods
            basket = Basket.objects.get(pk=request.POST['add_id'])
            try:
                good = Goods.objects.get(pk=basket.good_id)
                basket.quantity += 1
                error = check_basket_quantity(good, basket)
                basket.total_price = calculate_basket_total(good, basket)
                basket.save()
            except ObjectDoesNotExist:
                error = u"""Произошла ошибка при изменении количества товара. Возможно товар был удален из базы.
                Обратитесь к администратору или попробуйте заново."""
        elif 'substitute_id' in request.POST:
            # Substitute quantity in basket
            basket = Basket.objects.get(pk=request.POST['substitute_id'])
            try:
                good = Goods.objects.get(pk=basket.good_id)
                basket.quantity -= 1
                basket.total_price = calculate_basket_total(good, basket)
                basket.save()
                if basket.quantity == 0:
                    basket.delete()
            except ObjectDoesNotExist:
                error = u"""Произошла ошибка при изменении количества товара. Возможно товар был удален из базы.
                Обратитесь к администратору или попробуйте заново."""
        else:
            error = u"Неизвестная ошибка"
    baskets = Basket.objects.filter(client=client)
    total_summ = 0
    for basket in baskets:
        total_summ += basket.total_price
    return render_to_response('basket.html', {'client': client, 'baskets': baskets, 'error': error,
                                              'total_summ': total_summ}, context_instance=RequestContext(request))


@login_required()
def preview_order(request):
    """
    Preview order. step 1 - show goods.
    :param request: request object
    :return: HttpResponse.
    """
    error = ""
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
    baskets = Basket.objects.filter(client=client)
    for basket in baskets:
        if basket.stock_price == 0:
            basket.private_price = round((basket.total_price * float((100 - client.private_stock) / 100)), 2)
            basket.save()
    total_summ = calculate_basket_summ(baskets)
    return render_to_response('order.html', {'client': client, 'baskets': baskets, 'error': error,
                                             'total_summ': total_summ}, context_instance=RequestContext(request))


@login_required()
def choose_order_devmethod(request):
    """
    Choose delivery and payment method view.
    :param request:
    :return:
    """
    error = ""
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
    baskets = Basket.objects.filter(client=client)
    total_summ = calculate_basket_summ(baskets)
    form = ChoosePayDeliveryForm()
    dev_methods = DeliveryMethods.objects.all().order_by('cost')
    payments_methods = PaymentsMethods.objects.all()
    return render_to_response('order_s2.html', {'total_summ': total_summ, 'form': form, 'dev_methods': dev_methods,
                                                'payments_methods': payments_methods},
                              context_instance=RequestContext(request))


@login_required()
def choose_order_paymethod(request):
    """
    Enter delivery address and additional preview order
    :param request:
    :return:
    """
    if request.method == 'POST':
        error = ""
        try:
            user = User.objects.get(username=request.user.get_username())
            client = Clients.objects.get(login=user)
        except:
            error = "Клиента с такими параметрами не найдено."
        baskets = Basket.objects.filter(client=client)
        total_summ = calculate_basket_summ(baskets)
        try:
            dev_method = DeliveryMethods.objects.get(pk=request.POST['delivery_method'])
            pay_method = PaymentsMethods.objects.get(pk=request.POST['payment_method'])
        except:
            error = u"Выберите метод доставки"
            return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))
        request.session['delivery'] = dev_method.pk
        request.session['payment'] = pay_method.pk
        delivery_form = EnterDeliveryAddress(initial={
            'city': client.delivery_city, 'street': client.delivery_street, 'home': client.delivery_home,
            'office': client.delivery_office})
        if dev_method.id_method == 'kur' and total_summ > dev_method.cost:
            delivery_message = u"Ваша сумма заказа больше 5000. У вас бесплатная доставка."
        else:
            delivery_message = u"""Оплата доставки наличными курьеру. Подробнее о стоимости доставки можно прочитать в разделе Доставка и оплата."""
        return render_to_response('order_s3.html', {'dev_method': dev_method, 'pay_method': pay_method,
                                                    'baskets': baskets, 'delivery_message': delivery_message,
                                                    'total_summ': total_summ, 'delivery_form': delivery_form},
                                  context_instance=RequestContext(request))
    else:
        error = u"Ошибка в запросе. Попробуйте еще раз или обратитесь к администратору"
        return render_to_response('order_s3.html', {'error': error}, context_instance=RequestContext(request))


@login_required()
def cash_order(request):
    """
    Create order
    :param request:
    :return:
    """
    error = ""
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
    baskets = Basket.objects.filter(client=client)
    client_category = check_client_category(request)
    if baskets.exists():
        total_summ = calculate_basket_summ(baskets)
        delivery = DeliveryMethods.objects.get(pk=request.session['delivery'])
        payment = PaymentsMethods.objects.get(pk=request.session['payment'])
        order = Orders()
        order.client = client
        order.delivery = delivery
        order.order_sum = total_summ
        order.status = 0
        order.payments = payment
        order.created_date = timezone.now()
        order.save()
        # if delivery.id_method == 'kur':
        #     order.comments = u"Доставка курьером: стоимость {cost}".format(cost=delivery.cost)
        if request.method == 'POST':
            if 'city' in request.POST:
                order.delivery_city = request.POST['city']
                order.delivery_street = request.POST['street']
                order.delivery_home = request.POST['home']
                order.delivery_office = request.POST['office']
            else:
                error = u"Некорректно введен адрес доставки"
            if 'cl_name' in request.POST:
                cl_name = request.POST['cl_name']
            else:
                error = u"Некорректно введено ваше имя"
            if 'cl_phone' in request.POST:
                cl_phone = request.POST['cl_phone']
            else:
                error = u"Некорректно введен ваш телефон"
            order.comments = u"Контактное имя: " + cl_name + "\n" + u"Контактный телефон: " + cl_phone
        summ_order = 0
        order_detail_message = u"Позиция |\t Артикул |\t Количество |\t Цена \n"
        for basket in baskets:
            # Create order_details object
            order_detail = OrderDetails()
            order_detail.order = order
            order_detail.goods = basket.good
            order_detail.goods_pn = basket.good_pn
            order_detail.goods_id = basket.good_id
            order_detail.quantity = basket.quantity
            order_detail.meassure = basket.meassure
            try:
                good = Goods.objects.get(pk=basket.good_id)
            except:
                good = Goods.objects.get(partnumber=basket.good_pn)
            if good.stock_price != 0:
                order_detail.goods_price = good.stock_price
                order_detail.total_goods_price = good.stock_price * basket.quantity
            elif client.private_stock != 0:
                order_detail.goods_price = round((good.price * ((100 - client.private_stock)/100)), 2)
                order_detail.total_goods_price = order_detail.goods_price * order_detail.quantity
            else:
                if client_category is not None:
                    if client_category.code == "ip":
                        order_detail.goods_price = good.price_ip
                        order_detail.total_goods_price = good.price_ip * order_detail.quantity
                    elif client_category.code == "ltd":
                        order_detail.goods_price = good.price_org
                        order_detail.total_goods_price = good.price_org * order_detail.quantity
                    else:
                        order_detail.goods_price = good.price
                        order_detail.total_goods_price = good.price * order_detail.quantity
                else:
                    order_detail.goods_price = good.price
                    order_detail.total_goods_price = good.price * order_detail.quantity
            summ_order += order_detail.total_goods_price
            good.remainder -= basket.quantity
            good.reserved += basket.quantity
            good.save()
            order_detail.save()
            # order_detail_message += {}
            order_detail_message += u" {title} |\t {partnumber} |\t {quantity} |\t {price} \n".format(title=basket.good,
                                                                                               partnumber=basket.good_pn,
                                                                                               quantity=basket.quantity,
                                                                                                      price=str(order_detail.goods_price))
            basket.delete()
        order.order_sum = summ_order
        client.unpaid_sum += summ_order
        client.unpaid_orders += 1
        order.save()
        client.save()
        request.session['last_order_id'] = order.pk
        if payment.id_method == 'bill':
            # Create bill
            bill = Bills()
            bill.client = client
            bill.order = order
            bill.created_date = timezone.now()
            bill.save()
        else:
            bill = ''
        # Create email notifications
        email_subject = u"Оформлен заказ на сайте Sinkai Auto"
        email_subject2 = u"Пользователь оформил заказ на сайте"
        email_message = u"Здравствуйте! Оформлен заказ на сайте {host} № {order} \n Сумма: {summ} \n".format(
            summ=str(total_summ), order=str(order.pk), host=ALLOWED_HOSTS) + u"Позиции в заказе:\n" + \
                        order_detail_message + u" С уважением, \n Администрация интернет-магазина Синкай Авто"
        email_message2 = u"Заказ № {order} \n Сумма {summ} \n Клиент {client} \n".format(order=str(order.pk),
                                                                                    summ=str(total_summ),
                                                                                    client=client.title) + \
                         u"Позиции в заказе \n" + order_detail_message
        recipients = []
        recipients.append(user.email)
        admins = User.objects.filter(Q(groups__name="Менеджеры") | Q(groups__name="Администраторы") |
                                     Q(is_superuser=True))
        recipients2 = []
        for adm in admins:
            recipients2.append(adm.email)
        try:
            # Try to send email to user
            send_mail(email_subject, email_message, EMAIL_HOST_USER, recipients)
        except:
            error = u"Возникла непредвиденная ошибка! Попробуйте позднее"
        try:
            # Try to send email to admins
            send_mail(email_subject2, email_message2, EMAIL_HOST_USER, recipients2)
        except:
            pass
        order_desc = u"Покупка в магазине запчастей Синкай. Заказ № " + str(order.pk)
        form = RobokassaForm(initial={'OutSum': order.order_sum, 'InvId': order.pk, 'Desc': order_desc,
                                  'Email': user.email}, login=ROBOKASSA_LOGIN,
                         password1=ROBOKASSA_PASSWORD1, password2=ROBOKASSA_PASSWORD2)
        return render_to_response('order_self.html', {'delivery': delivery, 'payment': payment, 'bill': bill,
                                                  'total_summ': total_summ, 'order': order, 'form': form},
                              context_instance=RequestContext(request))
    else:
        error = u"В вашей корзине нет товаров. Возможно вы уже оформили заказ."
        return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))


# -------------------- Private office views -------------------------------------------

@login_required()
def lk(request):
    """
    Private office index view
    """
    if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
        return redirect('mgmt_index')
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
        return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))
    orders = Orders.objects.filter(client=client)
    return render_to_response('index_lk.html', {'client': client, 'orders': orders},
                              context_instance=RequestContext(request))


@login_required()
def edit_clients_lk(request):
    """
    Edit clients data by self
    :param request:
    :return: http response object
    """
    error = ""
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
        return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = lkEditClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
        else:
            error = u"Произошла ошибка при сохранении  данных"
    form = lkEditClientForm(instance=client)
    return render_to_response('lk_clients_edit.html', {'form': form, 'client': client, 'error': error},
                              context_instance=RequestContext(request))


@login_required()
def change_password_lk(request):
    """
    Change clients password by self
    :param request:
    :return: http response object
    """
    error = ""
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
        return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = ChangeClientPasswordEmailForm(request.POST)
        if form.is_valid():
            if request.POST["password1"] != '':
                pass1 = form.cleaned_data['password1']
                pass2 = form.cleaned_data['password2']
                if pass1 == pass2:
                    user.set_password(pass1)
                    user.save()
                else:
                    error = u"Пароли не совпадают. Попробуйте еще раз."
            elif request.POST['email'] != '':
                email = form.cleaned_data['email']
                user.email = email
                user.save()
            return redirect('lk-edit-client')
        else:
            error = u"Ошибка при заполнении формы. Попробуйте еще раз."
    form = ChangeClientPasswordEmailForm(initial={'email': user.email})
    return render_to_response('lk_clients_pass.html', {'form': form, 'user': user, 'client': client, 'error': error},
                              context_instance=RequestContext(request))


@login_required()
def lk_order(request, pk):
    """
    View order details in private office.
    :param request:
    :param pk: order id
    :return: HttpResponse
    """
    error = ""
    try:
        user = User.objects.get(username=request.user.get_username())
        client = Clients.objects.get(login=user)
    except:
        error = u"Клиента с такими параметрами не найдено."
        return render_to_response('error_page.html', {'error': error}, context_instance=RequestContext(request))
    order = get_object_or_404(Orders, pk=pk)
    if order.client != client:
        raise_403(request)
    if order.payments.id_method == 'bill':
        bill = Bills.objects.get(order=order)
    else:
        bill = ''
    order_desc = "Покупка в магазине запчастей Синкай. Заказ № " + str(order.pk)
    form = RobokassaForm(initial={'OutSum': order.order_sum, 'InvId': order.pk, 'Desc': order_desc,
                                  'Email': user.email}, login=ROBOKASSA_LOGIN,
                         password1=ROBOKASSA_PASSWORD1, password2=ROBOKASSA_PASSWORD2)
    orders_details = OrderDetails.objects.filter(order=order)
    return render_to_response('lk_orders.html', {'client': client, 'order': order, 'order_details': orders_details,
                                                 'error': error, 'form': form, 'bill': bill},
                              context_instance=RequestContext(request))


#-----------------------Pages views ---------------------------------------------------

def aboutcompany(request):
    """
    Show about company info
    :param request:
    :return:
    """
    page_about = get_object_or_404(AboutCompany, pk=1)
    return render_to_response('about_company.html', {'page_about': page_about},
                              context_instance=RequestContext(request))


def forsuppliers(request):
    """
    Show for suppliers info
    :param request:
    :return:
    """
    forsuppliers_page = get_object_or_404(ForSuppliers, pk=1)
    return render_to_response('forsuppliers.html', {'forsuppliers_page': forsuppliers_page},
                              context_instance=RequestContext(request))


def delivery_info(request):
    """
    Show delivery info
    :param request:
    :return:
    """
    delivery_page = get_object_or_404(DeliveryInfo, pk=1)
    return render_to_response('delivery_info.html', {'delivery_page': delivery_page},
                              context_instance=RequestContext(request))


def contacts(request):
    """
    Show contacts
    :param request:
    :return:
    """
    contact_page = get_object_or_404(Contacts, pk=1)
    return render_to_response('contact.html', {'contact_page': contact_page},
                              context_instance=RequestContext(request))


def faq_list(request):
    """
    Show faq list
    :param request:
    :return:
    """
    faqs = get_list_or_404(FAQ)
    return render_to_response('faq.html', {'faqs': faqs}, context_instance=RequestContext(request))


def pages(request, slug):
    """
    Show pages
    :param request:
    :param slug:
    :return:
    """
    page = Pages.objects.get(url=slug)
    return render_to_response('pages.html', {'page': page}, context_instance=RequestContext(request))

# ---------------------Added to fix bugs -------------------------------------


class FrontDeveloperListView(ListView):
    """
    Developers list for our store functionality
    """
    model = Developer
    template_name = 'developers_list.html'


def cat_list_with_dev(request, developer):
    """
    Shows categories list in front
    :param request: HttpRequest object
    :param developer: developer's title
    :return: HttpResponse object
    """
    client_category = check_client_category(request)
    categories = GoodsCategory.objects.all()
    developer = get_object_or_404(Developer, pk=developer)
    if client_category == None or client_category.code == "pv":
        price_opt = False
        goods = Goods.objects.filter(developer=developer).filter(price_list__opt=price_opt)
    else:
        goods = Goods.objects.filter(developer=developer)
    # if check_admin_group(request, "Администраторы") or check_admin_group(request, "Менеджеры"):
    #     goods = Goods.objects.filter(developer=developer)
    # else:
    #     goods = Goods.objects.filter(developer=developer).filter(price_list__opt=price_opt)
    return render_to_response('category_list.html', {'categories': categories, 'developer': developer, 'goods': goods},
                              context_instance=RequestContext(request))


def show_goods_cat_by_dev(request, developer, category):
    """
    Show goods list for developer and selected category
    :param request: HttpRequest object
    :param developer: developer's title
    :param category: categories title
    :return: HttpResponse object
    """
    client_category = check_client_category(request)
    dev = get_object_or_404(Developer, pk=developer)
    cat = get_object_or_404(GoodsCategory, pk=category)
    if client_category == None or client_category.code == "pv":
        price_opt = False
        goods = Goods.objects.filter(Q(developer=dev) & Q(category=cat) & Q(price_list__opt=price_opt))
    else:
        # price_opt = True
        goods = Goods.objects.filter(Q(developer=dev) & Q(category=cat))
    return render_to_response('goods_dev_cat.html', {'dev': dev, 'cat': cat, 'goods': goods,
                                                     'client_category': client_category},
                              context_instance=RequestContext(request))


def modal_good(request, pk):
    """
    Show good info
    :param request: request object
    :param pk: id of good
    :return: json object
    """
    good = get_object_or_404(Goods, pk=pk)
    good_json_dict = {
        'pk': good.pk,
        'partnumber': good.partnumber,
        'title': good.title,
        'description': good.description,
        'price': good.price,
    }
    if good.image == '':
        good_json_dict['image'] = ""
    else:
        # Create watermark image and get it url
        watermark_object = Watermarker()
        wm = watermark_object(good.image.url, 'watermark', position='C', opacity=0.2)
        good_json_dict['image'] = wm
    client_category = check_client_category(request)
    if client_category == None or client_category.code == "pv":
        good_json_dict['price'] = good.price
    else:
        good_json_dict['price'] = good.price_org
    return HttpResponse(json.dumps(good_json_dict))
