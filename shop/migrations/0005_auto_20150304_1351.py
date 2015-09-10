# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_markup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markup',
            name='title',
            field=models.CharField(null=True, blank=True, verbose_name='Название', max_length=256),
        ),
    ]
