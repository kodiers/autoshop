# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0063_auto_20150420_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientspricecategory',
            name='code',
            field=models.CharField(max_length=128, null=True, verbose_name=b'code', blank=True),
            preserve_default=True,
        ),
    ]
