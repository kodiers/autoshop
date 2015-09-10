# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_auto_20150316_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.TextField(null=True, verbose_name='Название', blank=True),
        ),
    ]
