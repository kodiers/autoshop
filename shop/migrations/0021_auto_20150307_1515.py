# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20150307_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='developer',
            options={'ordering': ['-title'], 'verbose_name': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c', 'verbose_name_plural': '\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438'},
        ),
        migrations.AlterModelOptions(
            name='goodscategory',
            options={'ordering': ['-title'], 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432'},
        ),
    ]
