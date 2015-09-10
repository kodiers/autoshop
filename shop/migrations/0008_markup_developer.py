# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20150304_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='markup',
            name='developer',
            field=models.ForeignKey(to='shop.Developer', null=True, blank=True, verbose_name='Производитель'),
            preserve_default=True,
        ),
    ]
