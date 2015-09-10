# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150304_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price_list',
            field=models.ForeignKey(null=True, verbose_name='Прайс-листы', blank=True, to='shop.PriceList'),
        ),
    ]
