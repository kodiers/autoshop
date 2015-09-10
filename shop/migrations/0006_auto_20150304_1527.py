# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150304_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price_list',
            field=models.ForeignKey(verbose_name='Прайс-листы', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.PriceList'),
        ),
    ]
