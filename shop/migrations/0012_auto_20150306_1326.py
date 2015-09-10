# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20150306_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='title',
            field=models.CharField(null=True, max_length=128, blank=True, verbose_name='Название'),
            preserve_default=True,
        ),
    ]
