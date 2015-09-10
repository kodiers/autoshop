# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_markup_modified_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='markup',
            options={'ordering': ['modified_date'], 'verbose_name_plural': 'Наценки', 'verbose_name': 'Торговая наценка'},
        ),
    ]
