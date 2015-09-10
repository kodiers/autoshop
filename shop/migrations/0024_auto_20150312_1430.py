# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20150312_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export1c',
            name='file',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb', blank=True),
        ),
    ]
