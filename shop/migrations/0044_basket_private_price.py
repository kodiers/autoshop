# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_basket_stock_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='private_price',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd1\x81 \xd1\x83\xd1\x87\xd0\xb5\xd1\x82\xd0\xbe\xd0\xbc \xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb8'),
            preserve_default=True,
        ),
    ]
