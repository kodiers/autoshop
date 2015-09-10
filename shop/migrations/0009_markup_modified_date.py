# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_markup_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='markup',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
            preserve_default=True,
        ),
    ]
