# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20150319_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='goods_id',
            field=models.IntegerField(null=True, verbose_name=b'ID \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
