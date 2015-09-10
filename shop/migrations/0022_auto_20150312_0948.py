# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20150307_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='export1c',
            options={'verbose_name': '\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u043e\u0441\u0442\u0430\u0442\u043a\u043e\u0432 \u0432 1\u0421', 'verbose_name_plural': '\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0438'},
        ),
        migrations.AddField(
            model_name='export1c',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='export1c',
            name='type',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb2\xd1\x8b\xd0\xb3\xd1\x80\xd1\x83\xd0\xb7\xd0\xba\xd0\xb8', choices=[(0, b'Goods'), (1, b'Orders')]),
            preserve_default=True,
        ),
    ]
