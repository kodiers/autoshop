# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_auto_20150324_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsmethods',
            name='id_method',
            field=models.CharField(max_length=32, null=True, verbose_name=b'ID', blank=True),
            preserve_default=True,
        ),
    ]
