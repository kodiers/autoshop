# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20150318_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcompany',
            name='ceo',
            field=models.TextField(null=True, verbose_name=b'\xd0\x94\xd0\xb8\xd1\x80\xd0\xb5\xd0\xba\xd1\x82\xd0\xbe\xd1\x80', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='law_address',
            field=models.TextField(null=True, verbose_name=b'\xd0\xae\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True),
        ),
    ]
