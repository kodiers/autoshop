# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_orders_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export1c',
            name='file',
            field=models.TextField(verbose_name='Файл', blank=True, null=True),
        ),
    ]
