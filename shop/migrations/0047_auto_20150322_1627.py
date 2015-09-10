# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_auto_20150322_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payments',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0', choices=[(0, b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xbf\xd1\x80\xd0\xb8 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb8'), (1, b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xbe\xd0\xb9'), (2, b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb3\xd0\xb0\xd0\xbc\xd0\xb8'), (3, b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xb8\xd0\xbc \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xbc'), (4, b'\xd0\x9f\xd0\xbe \xd1\x81\xd1\x87\xd0\xb5\xd1\x82\xd1\x83(\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x8e\xd1\x80 \xd0\xbb\xd0\xb8\xd1\x86)')]),
        ),
    ]
