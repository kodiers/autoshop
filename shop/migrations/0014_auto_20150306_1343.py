# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20150306_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='goodsCategory',
        ),
        migrations.AddField(
            model_name='stock',
            name='developer',
            field=models.ForeignKey(blank=True, verbose_name='Производитель', null=True, to='shop.Developer'),
            preserve_default=True,
        ),
    ]
