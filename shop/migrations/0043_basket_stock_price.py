# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20150321_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='stock_price',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xbe \xd0\xb0\xd0\xba\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=True,
        ),
    ]
