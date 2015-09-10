# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_markup_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x90\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f', blank=True, to='shop.Stock', null=True),
        ),
    ]
