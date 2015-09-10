# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0062_auto_20150420_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ['-date'], 'verbose_name': '\u041a\u043e\u0440\u0437\u0438\u043d\u0430', 'verbose_name_plural': '\u041a\u043e\u0440\u0437\u0438\u043d\u0430'},
        ),
    ]
