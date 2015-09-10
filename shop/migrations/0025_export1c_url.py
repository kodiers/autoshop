# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20150312_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='export1c',
            name='url',
            field=models.SlugField(null=True, verbose_name=b'URL', blank=True),
            preserve_default=True,
        ),
    ]
