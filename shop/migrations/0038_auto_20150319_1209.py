# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_orderdetails_meassure'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcompany',
            name='buh',
            field=models.TextField(null=True, verbose_name=b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb1\xd1\x83\xd1\x85\xd0\xb3\xd0\xb0\xd0\xbb\xd1\x82\xd0\xb5\xd1\x80', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='ceo',
            field=models.TextField(null=True, verbose_name=b'\xd0\x93\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb4\xd0\xb8\xd1\x80\xd0\xb5\xd0\xba\xd1\x82\xd0\xbe\xd1\x80', blank=True),
        ),
    ]
