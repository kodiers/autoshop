# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_auto_20150318_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='meassure',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x95\xd0\xb4. \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
    ]
