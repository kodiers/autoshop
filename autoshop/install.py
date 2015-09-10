# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0
# This script for install groups and create superuser (if not exist)
#
# -----------Default admin credentials:----------
# Login: admin
# Password: p@ssw0rd
#
# -----------------How-to run:-------------------
# root@~: python manage.py shell < sinkai/install.py


import os
import django
from watermarker.models import Watermark
from django.contrib.auth.models import Group, User
from shop.models import Contacts, AboutCompany, ForSuppliers, DeliveryInfo, PaymentsMethods, DeliveryMethods, \
    ClientsPriceCategory


def install_groups():
    groups = Group.objects.all()
    if not groups:
        Group.objects.create(name="Клиенты")
        Group.objects.create(name="Менеджеры")
        Group.objects.create(name="Администраторы")
        print("All groups created")
    else:
        if len(groups) < 3:
            group_names = ["Клиенты", "Менеджеры", "Администраторы"]
            for group in group_names:
                if not group in groups:
                    Group.objects.create(name=group)
            print("All groups created")
        print("All groups are exist")


def create_admin():
    admins = User.objects.filter(is_superuser=True)
    if not admins:
        admin = User.objects.create_superuser(username="admin", password="p@ssw0rd", email="admin@email.com")
        admin_group = Group.objects.get(name="Администраторы")
        admin.groups.add(admin_group)
        print("""Admin user created.
              Login: admin
              Password: p@ssw0rd
              email: admin@email.com
              You can change it from admin panel!"""
              )
    else:
        print("Administrator exist!")


def initialize_models():
    try:
        contact = Contacts()
        contact.phone = '+123456789'
        contact.zip = '123456'
        contact.address = 'Enter address please'
        contact.save()
        about_company = AboutCompany()
        about_company.title = 'О компании'
        about_company.content = 'Заполните информацией '
        about_company.bank_data = 'Заполните информацией '
        about_company.law_address = 'Заполните информацией '
        about_company.save()
        for_suppliers = ForSuppliers()
        for_suppliers.title = 'Информация для поставщиков'
        for_suppliers.content = 'Заполните информацией '
        for_suppliers.save()
        delivery_info = DeliveryInfo()
        delivery_info.title = 'Доставка и оплата'
        delivery_info.content = 'Заполните информацией '
        delivery_info.map = 'Заполните информацией '
        delivery_info.save()
        delivery_self = DeliveryMethods()
        delivery_self.title = "Самовывоз"
        delivery_self.description = "Самовывоз со склада в Москве"
        delivery_self.cost = 0
        delivery_self.id_method = "self"
        delivery_self.save()
        delivery_kurier = DeliveryMethods()
        delivery_kurier.title = "Курьерская доставка"
        delivery_kurier.description = "Доставка курьером по Москве"
        delivery_kurier.cost = 0
        delivery_kurier.id_method = "kur"
        delivery_kurier.save()
        payment_cash = PaymentsMethods()
        payment_cash.title = "Оплата наличными"
        payment_cash.description = "Оплата наличными при получении"
        payment_cash.id_method = "cash"
        payment_cash.save()
        payment_robo = PaymentsMethods()
        payment_robo.title = "Оплата электронным платежом"
        payment_robo.description = "Оплата через электронную систему RoboKassa"
        payment_robo.id_method = "robo"
        payment_robo.save()
        payment_bill = PaymentsMethods()
        payment_bill.title = "Оплата по счету"
        payment_bill.description = "Оплата безналичным платежом"
        payment_bill.id_method = "bill"
        payment_bill.save()
        private_person = ClientsPriceCategory()
        private_person.title = "Частное лицо"
        private_person.code = "pv"
        private_person.save()
        ip_client =  ClientsPriceCategory()
        ip_client.title = "Индивидуальный предприниматель"
        private_person.code = "ip"
        ip_client.save()
        organization = ClientsPriceCategory()
        organization.title = "Юридеческое лицо (ЗАО, ООО и тд.)"
        private_person.code = "ltd"
        organization.save()
        watermark = Watermark()
        watermark.name = "watermark"
        watermark.image = 'watermarks/logo.png'
        watermark.save()
        print("Models created successfully")
    except:
        print("Error! Couldn't create models.")


install_groups()
create_admin()
initialize_models()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sinkai.settings')
    django.setup()