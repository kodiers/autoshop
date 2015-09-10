# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20150312_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcompany',
            name='bank_data',
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='account',
            field=models.CharField(blank=True, max_length=128, verbose_name='Расчетный счет', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='bank_name',
            field=models.TextField(blank=True, null=True, verbose_name='Название банка'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='bik',
            field=models.CharField(blank=True, max_length=128, verbose_name='БИК', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='company_name',
            field=models.TextField(blank=True, null=True, verbose_name='Название компании'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='inn',
            field=models.CharField(blank=True, max_length=128, verbose_name='ИНН', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='kor_account',
            field=models.CharField(blank=True, max_length=128, verbose_name='Корреспондентский счет', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='kpp',
            field=models.CharField(blank=True, max_length=128, verbose_name='КПП', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='reg_data',
            field=models.TextField(blank=True, null=True, verbose_name='Сведения о регистрации'),
            preserve_default=True,
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
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='bill_status',
            field=models.BooleanField(default=False, verbose_name='Статус счета'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='client',
            field=models.ForeignKey(to='shop.Clients', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='modified_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='order',
            field=models.ForeignKey(to='shop.Orders', verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_address',
            field=models.TextField(blank=True, null=True, verbose_name='Контактный адрес'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_email',
            field=models.EmailField(max_length=75, verbose_name='Контактный email'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_name',
            field=models.CharField(blank=True, max_length=256, verbose_name='Контактное имя', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=128, verbose_name='Контактный телефон', null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='delivery_address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='is_org',
            field=models.BooleanField(default=False, verbose_name='Организационная форма'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='login',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='orders_sum',
            field=models.FloatField(default=0, verbose_name='Общая сумма заказов'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='preferred_payments',
            field=models.IntegerField(default=0, verbose_name='Предпочитаемый метод платежа', choices=[(0, 'Наличными курьеру'), (1, 'Банковской картой'), (2, 'Электронными деньгами'), (3, 'Банковским переводом'), (4, 'По счету(только для юр лиц)')]),
        ),
        migrations.AlterField(
            model_name='clients',
            name='private_stock',
            field=models.FloatField(default=0, verbose_name='Размер личной скидки'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='unpaid_orders',
            field=models.IntegerField(default=0, verbose_name='Количество неоплаченных заказов'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='unpaid_sum',
            field=models.FloatField(default=0, verbose_name='Задолженность'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(max_length=128, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='map',
            field=models.CharField(blank=True, max_length=256, verbose_name='Скрипт карты', null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=128, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='zip',
            field=models.CharField(max_length=12, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='map',
            field=models.CharField(blank=True, max_length=256, verbose_name='Скрипт карты', null=True),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выгрузки'),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='file',
            field=models.CharField(blank=True, max_length=256, verbose_name='Файл', null=True),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='title',
            field=models.CharField(blank=True, max_length=128, verbose_name='Название', null=True),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='type',
            field=models.IntegerField(default=0, verbose_name='Тип выгрузки', choices=[(0, 'Goods'), (1, 'Orders')]),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
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
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='Категория', to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='cost',
            field=models.FloatField(default=0.0, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='delivery_time',
            field=models.IntegerField(default=0, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='Производитель', to='shop.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='meassure',
            field=models.CharField(default='шт.', max_length=64, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='partnumber',
            field=models.CharField(blank=True, max_length=128, verbose_name='Артикул', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_list',
            field=models.ForeignKey(blank=True, verbose_name='Прайс-листы', to='shop.PriceList', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='remainder',
            field=models.IntegerField(default=0, verbose_name='Остаток на складе'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='reserved',
            field=models.IntegerField(default=0, verbose_name='Зарезервировано'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='show_on_index',
            field=models.BooleanField(default=False, verbose_name='Отображать на главной'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, verbose_name='Акция', to='shop.Stock', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock_price',
            field=models.FloatField(default=0.0, verbose_name='Цена по акции'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='supplier',
            field=models.ForeignKey(blank=True, verbose_name='Поставщик', to='shop.Supplier', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(blank=True, max_length=128, verbose_name='Название', null=True),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='markup',
            name='developer',
            field=models.ForeignKey(blank=True, verbose_name='Производитель', to='shop.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='goods_category',
            field=models.ForeignKey(blank=True, verbose_name='Категория товаров', to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='markup',
            name='pricelist',
            field=models.ForeignKey(blank=True, verbose_name='Прайс-лист', to='shop.PriceList', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='suppliers',
            field=models.ForeignKey(blank=True, verbose_name='Поставщик', to='shop.Supplier', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='title',
            field=models.CharField(blank=True, max_length=256, verbose_name='Название', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='value',
            field=models.FloatField(default=0, verbose_name='Размер наценки'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods',
            field=models.CharField(max_length=128, verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods_pn',
            field=models.CharField(max_length=128, verbose_name='Арктикул'),
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
            field=models.TextField(blank=True, null=True, verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivery_address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_sum',
            field=models.FloatField(default=0, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name='Статус платежа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Статус заказа', choices=[(0, 'Получен'), (1, 'В обработке'), (2, 'Сформирован'), (3, 'Отправлен')]),
        ),
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='image',
            field=models.ImageField(default=None, blank=True, upload_to='uploads', null=True, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='url',
            field=models.SlugField(verbose_name='Относительный URL'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='file',
            field=models.FileField(upload_to='pricelists', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='supplier',
            field=models.ForeignKey(to='shop.Supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='developer',
            field=models.ForeignKey(blank=True, verbose_name='Производитель', to='shop.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='goods_category',
            field=models.ForeignKey(blank=True, verbose_name='Категория товаров', to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='show_on_main_page',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='title',
            field=models.CharField(blank=True, max_length=128, verbose_name='Название', null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.FloatField(default=0, verbose_name='Размер скидки'),
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
            field=models.EmailField(blank=True, max_length=75, verbose_name='Контактный email', null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=64, verbose_name='Контактный телефон', null=True),
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
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]
