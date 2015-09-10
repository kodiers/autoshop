# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150304_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Markup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128, blank=True, verbose_name='Название', null=True)),
                ('value', models.FloatField(default=0, verbose_name='Размер наценки')),
                ('goods', models.ManyToManyField(blank=True, verbose_name='Товары', null=True, to='shop.Goods')),
                ('goods_category', models.ForeignKey(to='shop.GoodsCategory', blank=True, verbose_name='Категория товаров', null=True)),
                ('pricelist', models.ForeignKey(to='shop.PriceList', blank=True, verbose_name='Прайс-лист', null=True)),
                ('suppliers', models.ForeignKey(to='shop.Supplier', blank=True, verbose_name='Поставщик', null=True)),
            ],
            options={
                'verbose_name': 'Торговая наценка',
                'verbose_name_plural': 'Наценки',
            },
            bases=(models.Model,),
        ),
    ]
