# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0056_auto_20150415_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='clients',
            name='is_org',
        ),
        migrations.AddField(
            model_name='clients',
            name='clients_category',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='shop.ClientsCategory', null=True),
            preserve_default=True,
        ),
    ]
