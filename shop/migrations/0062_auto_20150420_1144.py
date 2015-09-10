# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0061_goods_internal_partnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='good',
            field=models.TextField(max_length=128, null=True, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods',
            field=models.TextField(max_length=128, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80'),
        ),
    ]
