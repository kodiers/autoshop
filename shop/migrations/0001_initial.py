# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=128)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('bank_data', models.TextField(verbose_name='Банковские реквизиты')),
                ('law_address', models.TextField(verbose_name='Юридический адрес')),
                ('modified_date', models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_date', models.DateField(verbose_name='Дата создания', default=django.utils.timezone.now)),
                ('modified_date', models.DateField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
                ('bill_status', models.BooleanField(verbose_name='Статус счета', default=False)),
                ('comments', models.TextField(verbose_name='Комментарии', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=256)),
                ('contact_name', models.CharField(verbose_name='Контактное имя', blank=True, max_length=256, null=True)),
                ('contact_address', models.TextField(verbose_name='Контактный адрес', blank=True, null=True)),
                ('contact_phone', models.CharField(verbose_name='Контактный телефон', blank=True, max_length=128, null=True)),
                ('contact_email', models.EmailField(verbose_name='Контактный email', max_length=75)),
                ('is_org', models.BooleanField(verbose_name='Организационная форма', default=False)),
                ('delivery_address', models.TextField(verbose_name='Адрес доставки', blank=True, null=True)),
                ('preferred_payments', models.IntegerField(verbose_name='Предпочитаемый метод платежа', choices=[(0, 'Наличными курьеру'), (1, 'Банковской картой'), (2, 'Электронными деньгами'), (3, 'Банковским переводом'), (4, 'По счету(только для юр лиц)')], default=0)),
                ('private_stock', models.FloatField(verbose_name='Размер личной скидки', default=0)),
                ('orders_sum', models.FloatField(verbose_name='Общая сумма заказов', default=0)),
                ('unpaid_orders', models.IntegerField(verbose_name='Количество неоплаченных заказов', default=0)),
                ('unpaid_sum', models.FloatField(verbose_name='Задолженность', default=0)),
                ('registration_date', models.DateField(verbose_name='Дата регистрации', default=django.utils.timezone.now)),
                ('login', models.ForeignKey(verbose_name='Логин', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('phone', models.CharField(verbose_name='Телефон', max_length=128)),
                ('zip', models.CharField(verbose_name='Почтовый индекс', max_length=12)),
                ('address', models.CharField(verbose_name='Адрес', max_length=128)),
                ('email', models.EmailField(default='test@test.ru', max_length=75)),
                ('map', models.CharField(verbose_name='Скрипт карты', blank=True, max_length=256, null=True)),
                ('comments', models.TextField(verbose_name='Комментарии', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Контакты',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeliveryInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=128)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('map', models.CharField(verbose_name='Скрипт карты', blank=True, max_length=256, null=True)),
                ('modified_date', models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Доставка и оплата',
                'verbose_name_plural': 'Доставка и оплата',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=128)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Export1C',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file', models.CharField(verbose_name='Файл', max_length=256)),
                ('date', models.DateTimeField(verbose_name='Дата выгрузки', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Выгрузка в 1С',
                'verbose_name_plural': 'Выгрузки',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('modified_date', models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'FAQ',
                'ordering': ['-modified_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForSuppliers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=128)),
                ('content', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('modified_date', models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Поставщикам',
                'verbose_name_plural': 'Поставщикам',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('partnumber', models.CharField(verbose_name='Артикул', blank=True, max_length=128, null=True)),
                ('title', models.CharField(verbose_name='Название', blank=True, max_length=128, null=True)),
                ('description', models.TextField(verbose_name='Описание', blank=True, null=True)),
                ('show_on_index', models.BooleanField(verbose_name='Отображать на главной', default=False)),
                ('remainder', models.IntegerField(verbose_name='Остаток на складе', default=0)),
                ('reserved', models.IntegerField(verbose_name='Зарезервировано', default=0)),
                ('delivery_time', models.IntegerField(verbose_name='Время доставки', default=0)),
                ('meassure', models.CharField(verbose_name='Единица измерения', default='шт.', max_length=64)),
                ('price', models.FloatField(verbose_name='Цена', default=0.0)),
                ('cost', models.FloatField(verbose_name='Стоимость', default=0.0)),
                ('stock_price', models.FloatField(verbose_name='Цена по акции', default=0.0)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=128)),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Markup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.FloatField(verbose_name='Размер наценки', default=0)),
                ('goods', models.ManyToManyField(verbose_name='Товары', blank=True, to='shop.Goods', null=True)),
            ],
            options={
                'verbose_name': 'Торговая наценка',
                'verbose_name_plural': 'Наценки',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('goods', models.CharField(verbose_name='Товар', max_length=128)),
                ('goods_pn', models.CharField(verbose_name='Арктикул', max_length=128)),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('goods_price', models.FloatField(verbose_name='Цена за единицу')),
                ('total_goods_price', models.FloatField(verbose_name='Общая цена')),
            ],
            options={
                'verbose_name': 'Детали заказа',
                'verbose_name_plural': 'Детали заказов',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('order_sum', models.FloatField(verbose_name='Сумма заказа', default=0)),
                ('delivery_address', models.TextField(verbose_name='Адрес доставки', blank=True, null=True)),
                ('status', models.IntegerField(verbose_name='Статус заказа', choices=[(0, 'Получен'), (1, 'В обработке'), (2, 'Сформирован'), (3, 'Отправлен')], default=0)),
                ('payment_status', models.BooleanField(verbose_name='Статус платежа', default=False)),
                ('created_date', models.DateTimeField(verbose_name='Дата создания заказа', default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
                ('comments', models.TextField(verbose_name='Комментарии', blank=True, null=True)),
                ('client', models.ForeignKey(verbose_name='Клиент', to='shop.Clients')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=128)),
                ('url', models.SlugField(verbose_name='Относительный URL')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('image', models.ImageField(verbose_name='Изображение', blank=True, default=None, upload_to='uploads', null=True)),
                ('created_date', models.DateTimeField(verbose_name='Дата создания', default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(verbose_name='Дата изменения', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Страница сайта',
                'verbose_name_plural': 'Страницы сайта',
                'ordering': ['-modified_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file', models.FileField(verbose_name='Файл', upload_to='pricelists')),
                ('date', models.DateTimeField(verbose_name='Дата загрузки', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Прайс-лист',
                'verbose_name_plural': 'Прайс-листы',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.FloatField(verbose_name='Размер скидки', default=0)),
                ('show_on_main_page', models.BooleanField(verbose_name='Показывать на главной', default=False)),
                ('due_on_date', models.DateField(verbose_name='Акция истекает', default=django.utils.timezone.now)),
                ('goods', models.ManyToManyField(verbose_name='Товары', blank=True, to='shop.Goods', null=True)),
                ('goodsCategory', models.ManyToManyField(verbose_name='Категория товаров', blank=True, to='shop.GoodsCategory', null=True)),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=256)),
                ('bank_data', models.TextField(verbose_name='Банковские реквизиты')),
                ('law_address', models.TextField(verbose_name='Юридический адрес')),
                ('fact_address', models.TextField(verbose_name='Фактический адрес')),
                ('contact', models.TextField(verbose_name='Контактное лицо')),
                ('contact_phone', models.CharField(verbose_name='Контактный телефон', blank=True, max_length=64, null=True)),
                ('contact_email', models.EmailField(verbose_name='Контактный email', blank=True, max_length=75, null=True)),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='supplier',
            field=models.ForeignKey(verbose_name='Поставщик', to='shop.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(verbose_name='Заказ', to='shop.Orders'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='markup',
            name='suppliers',
            field=models.ManyToManyField(verbose_name='Поставщики', blank=True, to='shop.Supplier', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(verbose_name='Категория', to='shop.GoodsCategory', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='developer',
            field=models.ForeignKey(verbose_name='Производитель', to='shop.Developer', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='price_list_new',
            field=models.ForeignKey(verbose_name='Прайс-листы', to='shop.PriceList', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='supplier',
            field=models.ForeignKey(verbose_name='Поставщик', to='shop.Supplier', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bills',
            name='client',
            field=models.ForeignKey(verbose_name='Клиент', to='shop.Clients'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bills',
            name='order',
            field=models.ForeignKey(verbose_name='Номер заказа', to='shop.Orders'),
            preserve_default=True,
        ),
    ]
