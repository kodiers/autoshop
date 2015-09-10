# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20150314_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bills',
            options={'ordering': ['-modified_date'], 'verbose_name': 'Счет', 'verbose_name_plural': 'Счета'},
        ),
    ]
