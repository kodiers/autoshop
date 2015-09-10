# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0041_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
