# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0050_auto_20150324_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverymethods',
            name='id_method',
            field=models.CharField(max_length=32, null=True, verbose_name=b'ID', blank=True),
            preserve_default=True,
        ),
    ]
