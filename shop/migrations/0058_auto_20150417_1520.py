# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0057_auto_20150417_1502'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientsCategory',
            new_name='ClientsPriceCategory',
        ),
        migrations.AlterModelOptions(
            name='clientspricecategory',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0446\u0435\u043d\u044b', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0446\u0435\u043d\u044b'},
        ),
        migrations.AddField(
            model_name='clients',
            name='is_org',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='clients',
            name='clients_category',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd1\x8b', blank=True, to='shop.ClientsPriceCategory', null=True),
        ),
    ]
