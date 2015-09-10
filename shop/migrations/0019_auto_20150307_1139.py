# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150307_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='shop.Developer', null=True),
        ),
    ]
