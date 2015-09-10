# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django import forms
from shop.models import Clients, Pages, PriceList, Markup, Stock, GoodsCategory, Developer, Export1C, Orders, Bills, \
    DeliveryMethods, PaymentsMethods
from ckeditor.widgets import CKEditorWidget


class ClientRegistrationForm(forms.Form):
    """
    Form for registration client
    """
    login = forms.CharField(max_length=128, label='Логин')
    password1 = forms.CharField(label="Введите пароль", widget=forms.PasswordInput, min_length=8, max_length=128)
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, min_length=8, max_length=128)
    email = forms.EmailField(label="Адрес электронной почты", max_length=100)
    title = forms.CharField(label="Ваше имя:", max_length=256)
    phone = forms.CharField(label="Контактный телефон", max_length=100)


class OrgClientRegistrationForm(forms.Form):
    """
    Form for registration organizations
    """
    login = forms.CharField(max_length=128, label='Логин')
    password1 = forms.CharField(label="Введите пароль", widget=forms.PasswordInput, min_length=8, max_length=128)
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, min_length=8, max_length=128)
    email = forms.EmailField(label="Адрес электронной почты", max_length=100)
    # clients_category = forms.ChoiceField(choices=ClientsCategory.objects.exclude("Частное лицо").values_list(),
    #                                      label="Выберите организационно-правовую форму")
    title = forms.CharField(label="Название организации", max_length=256)
    phone = forms.CharField(label="Контактный телефон", max_length=100)
    contact_name = forms.CharField(label="Контактное лицо", max_length=256)
    law_data = forms.CharField(widget=forms.Textarea, label="Банковские реквизиты")
    law_address = forms.CharField(widget=forms.Textarea, label="Юридический адрес")


class RestorePasswordForm(forms.Form):
    """
    Form for send email with new password to user
    """
    email_field = forms.EmailField(label=u'Введите адрес электронной почты', max_length=100)


class UploadPriceListForm(forms.ModelForm):
    """
    Form for save uploaded pricelist.
    """
    class Meta:
        model = PriceList
        fields = ['supplier', 'file', 'date', 'opt']


class CreateMarkupByPropertyForm(forms.ModelForm):
    """
    Form for create markup
    """
    # choice_category = ((0, 'Поставщик'), (1, 'Прайс-лис'), (2, 'Категория товаров'), (3, 'Производитель'))
    # category = forms.TypedChoiceField(choices=choice_category, widget=forms.RadioSelect, coerce=int, label='Признак наценки')
    class Meta:
        model = Markup
        fields = ['title', 'suppliers', 'pricelist', 'goods_category', 'developer', 'value', 'modified_date']


class CreateStockForm(forms.ModelForm):
    """
    Create stock model form
    """
    # goods_select = forms.ModelMultipleChoiceField(queryset=Goods.objects.all(), required=False,
    #                                               widget=forms.CheckboxSelectMultiple, label='Товары в акции')
    class Meta:
        model = Stock
        exclude = ['goods']


class EditDeveloperForm(forms.ModelForm):
    """
    Edit developer form
    """
    class Meta:
        model = Developer
        fields = ['title']


class EditCategoryForm(forms.ModelForm):
    """
    Edit category form
    """
    class Meta:
        model = GoodsCategory
        fields = ['title']


class NewExport1CGoodsForm(forms.ModelForm):
    """
    Export 1C goods form
    """
    class Meta:
        model = Export1C
        fields = ['title', 'date']


class ChangeClientPasswordEmailForm(forms.Form):
    """
    Change password form
    """
    email = forms.EmailField(label='Адрес электронной почты', max_length=100, required=False)
    password1 = forms.CharField(label="Введите пароль", widget=forms.PasswordInput, min_length=8, max_length=30, required=False)
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, min_length=8, max_length=30, required=False)


class ChangeOrderForm(forms.ModelForm):
    """
    Change order form
    """
    class Meta:
        model = Orders
        fields = ['delivery_zip', 'delivery_city', 'delivery_street', 'delivery_home', 'delivery_office', 'status',
                  'payment_status', 'payments', 'delivery', 'comments', 'modified_date']
        labels = {
            'payment_status': "Оплата получена: ",
        }


class BillsChangeForm(forms.ModelForm):
    """
    Change bill form
    """
    class Meta:
        model = Bills
        fields = ['bill_status', 'comments']
        labels = {
            'bill_status': "Счет оплачен: ",
        }


class AdmUserChangeForm(UserChangeForm):
    """
    Change administrator or manager form
    """
    group = forms.ChoiceField(choices=Group.objects.exclude(name="Клиенты").values_list(), label="Выберите группу", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser', 'password']


class AdminCreateForm(UserCreationForm):
    """
    Form for create manager or administrator
    """
    group = forms.ChoiceField(choices=Group.objects.exclude(name="Клиенты").values_list(), label="Выберите группу",
                              required=True)
    def __init__(self, *args, **kwargs):
        super(AdminCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'email')


class ChoosePayDeliveryForm(forms.Form):
    """
    Choose delivery method form in create order
    """
    delivery_method = forms.ModelChoiceField(queryset=DeliveryMethods.objects.all(), label="Выберите метод доставки")
    payment_method = forms.ModelChoiceField(queryset=PaymentsMethods.objects.all(), label="Выберите метод оплаты")


class EnterDeliveryAddress(forms.Form):
    # zip = forms.CharField(max_length=32, label="Индекс", required=False) Commented for future use
    city = forms.CharField(max_length=128, label="Город", required=True)
    street = forms.CharField(label="Улица доставки", widget=forms.Textarea(attrs={'width':"128px", 'cols': 20}), required=True)
    home = forms.CharField(label="Номер и корпус дома", required=True, max_length=128)
    office = forms.CharField(max_length=16, label="Номер квартиры/офиса", required=False)


class lkEditClientForm(forms.ModelForm):
    """
    Form for edit clients data by self.
    """
    class Meta:
        model = Clients
        fields = ['title', 'contact_name', 'contact_address', 'contact_phone', 'contact_email', 'delivery_zip',
              'delivery_city', 'delivery_street', 'delivery_home', 'delivery_office', 'preferred_payments', 'law_data',
              'law_address', 'is_org']
        labels = {
            'is_org': "Отметьте, если являетесь юридическим лицом: ",
        }


# ########### Not used in this version ###############################

class PagesModelForm(forms.ModelForm):
    """
    Model form for Pages to use CKeditor WYSWYG
    """
    content = forms.CharField(widget=CKEditorWidget(), label='Текст')
    class Meta:
        model = Pages
        fields = ('title', 'url', 'content', 'image', 'modified_date')


class ChoosePaymentMethodForm(forms.Form):
    """
    Choose payment method form
    """
    payment_method = forms.ModelChoiceField(queryset=PaymentsMethods.objects.all(), label="Выберите метод оплаты")