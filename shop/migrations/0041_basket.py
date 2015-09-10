# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_orderdetails_goods_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('good_id', models.IntegerField(verbose_name=b'ID \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0')),
                ('good_pn', models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x90\xd1\x80\xd1\x82\xd0\xb8\xd0\xba\xd1\x83\xd0\xbb', blank=True)),
                ('good', models.CharField(max_length=128, null=True, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80', blank=True)),
                ('quantity', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('meassure', models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x95\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('good_price', models.FloatField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb7\xd0\xb0 \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd1\x83')),
                ('total_price', models.FloatField(verbose_name=b'\xd0\xa1\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82', blank=True, to='shop.Clients', null=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u0440\u0437\u0438\u043d\u0430',
                'verbose_name_plural': '\u041a\u043e\u0440\u0437\u0438\u043d\u0430',
            },
            bases=(models.Model,),
        ),
    ]
