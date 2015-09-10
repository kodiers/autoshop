# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0060_auto_20150417_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='internal_partnumber',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x92\xd0\xbd\xd1\x83\xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xba\xd1\x83\xd0\xbb', blank=True),
            preserve_default=True,
        ),
    ]
