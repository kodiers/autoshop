# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_auto_20150329_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bills',
            options={'ordering': ['-pk'], 'verbose_name': '\u0421\u0447\u0435\u0442', 'verbose_name_plural': '\u0421\u0447\u0435\u0442\u0430'},
        ),
    ]
