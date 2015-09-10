# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0049_paymentsmethods_id_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsmethods',
            name='id_method',
            field=models.CharField(max_length=32, verbose_name=b'ID'),
        ),
    ]
