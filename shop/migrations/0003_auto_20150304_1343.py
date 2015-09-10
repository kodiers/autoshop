# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150304_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markup',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='markup',
            name='suppliers',
        ),
        migrations.DeleteModel(
            name='Markup',
        ),
    ]
