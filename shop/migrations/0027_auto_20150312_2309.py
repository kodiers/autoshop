# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20150312_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиент', 'ordering': ['title'], 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'ordering': ['-modified_date'], 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='bank_data',
            field=models.TextField(verbose_name='Банковские реквизиты'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='law_address',
            field=models.TextField(verbose_name='Юридический адрес'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='title',
            field=models.CharField(verbose_name='Заголовок', max_length=128),
        ),
        migrations.AlterField(
            model_name='bills',
            name='bill_status',
            field=models.BooleanField(verbose_name='Статус счета', default=False),
        ),
        migrations.AlterField(
            model_name='bills',
            name='client',
            field=models.ForeignKey(to='shop.Clients', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='comments',
            field=models.TextField(verbose_name='Комментарии', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='created_date',
            field=models.DateField(verbose_name='Дата создания', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bills',
            name='modified_date',
            field=models.DateField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bills',
            name='order',
            field=models.ForeignKey(to='shop.Orders', verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_address',
            field=models.TextField(verbose_name='Контактный адрес', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_email',
            field=models.EmailField(verbose_name='Контактный email', max_length=75),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_name',
            field=models.CharField(verbose_name='Контактное имя', null=True, blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_phone',
            field=models.CharField(verbose_name='Контактный телефон', null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='clients',
            name='delivery_address',
            field=models.TextField(verbose_name='Адрес доставки', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='is_org',
            field=models.BooleanField(verbose_name='Организационная форма', default=False),
        ),
        migrations.AlterField(
            model_name='clients',
            name='login',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='orders_sum',
            field=models.FloatField(verbose_name='Общая сумма заказов', default=0),
        ),
        migrations.AlterField(
            model_name='clients',
            name='preferred_payments',
            field=models.IntegerField(verbose_name='Предпочитаемый метод платежа', choices=[(0, 'Наличными курьеру'), (1, 'Банковской картой'), (2, 'Электронными деньгами'), (3, 'Банковским переводом'), (4, 'По счету(только для юр лиц)')], default=0),
        ),
        migrations.AlterField(
            model_name='clients',
            name='private_stock',
            field=models.FloatField(verbose_name='Размер личной скидки', default=0),
        ),
        migrations.AlterField(
            model_name='clients',
            name='registration_date',
            field=models.DateField(verbose_name='Дата регистрации', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clients',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=256),
        ),
        migrations.AlterField(
            model_name='clients',
            name='unpaid_orders',
            field=models.IntegerField(verbose_name='Количество неоплаченных заказов', default=0),
        ),
        migrations.AlterField(
            model_name='clients',
            name='unpaid_sum',
            field=models.FloatField(verbose_name='Задолженность', default=0),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=128),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='comments',
            field=models.TextField(verbose_name='Комментарии', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='map',
            field=models.CharField(verbose_name='Скрипт карты', null=True, blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=128),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='zip',
            field=models.CharField(verbose_name='Почтовый индекс', max_length=12),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='map',
            field=models.CharField(verbose_name='Скрипт карты', null=True, blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='title',
            field=models.CharField(verbose_name='Заголовок', max_length=128),
        ),
        migrations.AlterField(
            model_name='developer',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=128),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='date',
            field=models.DateTimeField(verbose_name='Дата выгрузки', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='file',
            field=models.CharField(verbose_name='Файл', null=True, blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='title',
            field=models.CharField(verbose_name='Название', null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='type',
            field=models.IntegerField(verbose_name='Тип выгрузки', choices=[(0, 'Goods'), (1, 'Orders')], default=0),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='url',
            field=models.SlugField(verbose_name='URL', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='title',
            field=models.CharField(verbose_name='Заголовок', max_length=128),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.GoodsCategory', verbose_name='Категория', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='cost',
            field=models.FloatField(verbose_name='Стоимость', default=0.0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='delivery_time',
            field=models.IntegerField(verbose_name='Время доставки', default=0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(verbose_name='Описание', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Developer', verbose_name='Производитель', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='meassure',
            field=models.CharField(verbose_name='Единица измерения', default='шт.', max_length=64),
        ),
        migrations.AlterField(
            model_name='goods',
            name='partnumber',
            field=models.CharField(verbose_name='Артикул', null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.FloatField(verbose_name='Цена', default=0.0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_list',
            field=models.ForeignKey(null=True, to='shop.PriceList', verbose_name='Прайс-листы', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='remainder',
            field=models.IntegerField(verbose_name='Остаток на складе', default=0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='reserved',
            field=models.IntegerField(verbose_name='Зарезервировано', default=0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='show_on_index',
            field=models.BooleanField(verbose_name='Отображать на главной', default=False),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Stock', verbose_name='Акция', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock_price',
            field=models.FloatField(verbose_name='Цена по акции', default=0.0),
        ),
        migrations.AlterField(
            model_name='goods',
            name='supplier',
            field=models.ForeignKey(null=True, to='shop.Supplier', verbose_name='Поставщик', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(verbose_name='Название', null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=128),
        ),
        migrations.AlterField(
            model_name='markup',
            name='developer',
            field=models.ForeignKey(null=True, to='shop.Developer', verbose_name='Производитель', blank=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='goods_category',
            field=models.ForeignKey(null=True, to='shop.GoodsCategory', verbose_name='Категория товаров', blank=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='markup',
            name='pricelist',
            field=models.ForeignKey(null=True, to='shop.PriceList', verbose_name='Прайс-лист', blank=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='suppliers',
            field=models.ForeignKey(null=True, to='shop.Supplier', verbose_name='Поставщик', blank=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='title',
            field=models.CharField(verbose_name='Название', null=True, blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='markup',
            name='value',
            field=models.FloatField(verbose_name='Размер наценки', default=0),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods',
            field=models.CharField(verbose_name='Товар', max_length=128),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods_pn',
            field=models.CharField(verbose_name='Арктикул', max_length=128),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods_price',
            field=models.FloatField(verbose_name='Цена за единицу'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(to='shop.Orders', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='total_goods_price',
            field=models.FloatField(verbose_name='Общая цена'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='client',
            field=models.ForeignKey(to='shop.Clients', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='comments',
            field=models.TextField(verbose_name='Комментарии', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания заказа', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivery_address',
            field=models.TextField(verbose_name='Адрес доставки', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_sum',
            field=models.FloatField(verbose_name='Сумма заказа', default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_status',
            field=models.BooleanField(verbose_name='Статус платежа', default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(verbose_name='Статус заказа', choices=[(0, 'Получен'), (1, 'В обработке'), (2, 'Сформирован'), (3, 'Отправлен')], default=0),
        ),
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pages',
            name='image',
            field=models.ImageField(null=True, default=None, verbose_name='Изображение', blank=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(verbose_name='Заголовок', max_length=128),
        ),
        migrations.AlterField(
            model_name='pages',
            name='url',
            field=models.SlugField(verbose_name='Относительный URL'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='date',
            field=models.DateTimeField(verbose_name='Дата загрузки', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='file',
            field=models.FileField(verbose_name='Файл', upload_to='pricelists'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='supplier',
            field=models.ForeignKey(to='shop.Supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='developer',
            field=models.ForeignKey(null=True, to='shop.Developer', verbose_name='Производитель', blank=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='goods_category',
            field=models.ForeignKey(null=True, to='shop.GoodsCategory', verbose_name='Категория товаров', blank=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='stock',
            name='show_on_main_page',
            field=models.BooleanField(verbose_name='Показывать на главной', default=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='title',
            field=models.CharField(verbose_name='Название', null=True, blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.FloatField(verbose_name='Размер скидки', default=0),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='bank_data',
            field=models.TextField(verbose_name='Банковские реквизиты'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact',
            field=models.TextField(verbose_name='Контактное лицо'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_email',
            field=models.EmailField(verbose_name='Контактный email', null=True, blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_phone',
            field=models.CharField(verbose_name='Контактный телефон', null=True, blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fact_address',
            field=models.TextField(verbose_name='Фактический адрес'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='law_address',
            field=models.TextField(verbose_name='Юридический адрес'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=256),
        ),
    ]
