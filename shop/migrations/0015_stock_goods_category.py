# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20150306_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='goods_category',
            field=models.ForeignKey(null=True, blank=True, to='shop.GoodsCategory', verbose_name='Категория товаров'),
            preserve_default=True,
        ),
    ]
