# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20150306_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='due_on_date',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='start_date',
        ),
        migrations.AddField(
            model_name='stock',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения'),
            preserve_default=True,
        ),
    ]
