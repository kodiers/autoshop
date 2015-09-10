# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_export1c_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='export1c',
            options={'ordering': ['-date'], 'verbose_name': '\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u043e\u0441\u0442\u0430\u0442\u043a\u043e\u0432 \u0432 1\u0421', 'verbose_name_plural': '\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0438'},
        ),
    ]
