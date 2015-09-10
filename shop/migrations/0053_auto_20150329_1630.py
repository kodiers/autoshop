# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0052_auto_20150325_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='bank_data',
            field=models.TextField(null=True, verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb2\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbb\xd0\xb8\xd1\x86\xd0\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fact_address',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='law_address',
            field=models.TextField(null=True, verbose_name=b'\xd0\xae\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True),
        ),
    ]
