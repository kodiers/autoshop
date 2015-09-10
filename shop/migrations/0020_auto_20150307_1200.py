# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20150307_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-modified_date'], 'verbose_name': '\u0410\u043a\u0446\u0438\u044f', 'verbose_name_plural': '\u0410\u043a\u0446\u0438\u0438'},
        ),
    ]
