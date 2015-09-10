# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_auto_20150321_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='delivery_address',
        ),
        migrations.AddField(
            model_name='clients',
            name='delivery_city',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='delivery_home',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb8 \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd1\x83\xd1\x81 \xd0\xb4\xd0\xbe\xd0\xbc\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='delivery_office',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xba\xd0\xb2\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd1\x80\xd1\x8b/\xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='delivery_street',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clients',
            name='delivery_zip',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb8\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_city',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_home',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb8 \xd0\xba\xd0\xbe\xd1\x80\xd0\xbf\xd1\x83\xd1\x81 \xd0\xb4\xd0\xbe\xd0\xbc\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_office',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xba\xd0\xb2\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd1\x80\xd1\x8b/\xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_street',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_zip',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb8\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81\xd0\xb0 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
    ]
