# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import ckeditor.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20150316_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='law_data',
            field=models.TextField(null=True, verbose_name=b'\xd0\xae\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='account',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x87\xd0\xb5\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x87\xd0\xb5\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='bank_name',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb1\xd0\xb0\xd0\xbd\xd0\xba\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='bik',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x91\xd0\x98\xd0\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='company_name',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='inn',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x98\xd0\x9d\xd0\x9d', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='kor_account',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd1\x80\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd1\x81\xd1\x87\xd0\xb5\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='kpp',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9a\xd0\x9f\xd0\x9f', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='law_address',
            field=models.TextField(verbose_name=b'\xd0\xae\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='reg_data',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa1\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='bill_status',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd1\x81\xd1\x87\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='client',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82', to='shop.Clients'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='comments',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='bills',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='modified_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='bills',
            name='order',
            field=models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0', to='shop.Orders'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_address',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_email',
            field=models.EmailField(max_length=75, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 email'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_name',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb8\xd0\xbc\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='contact_phone',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='delivery_address',
            field=models.TextField(null=True, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='is_org',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='login',
            field=models.ForeignKey(verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clients',
            name='orders_sum',
            field=models.FloatField(default=0, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb0\xd1\x8f \xd1\x81\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='preferred_payments',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbf\xd0\xbe\xd1\x87\xd0\xb8\xd1\x82\xd0\xb0\xd0\xb5\xd0\xbc\xd1\x8b\xd0\xb9 \xd0\xbc\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0', choices=[(0, b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xba\xd1\x83\xd1\x80\xd1\x8c\xd0\xb5\xd1\x80\xd1\x83'), (1, b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xbe\xd0\xb9'), (2, b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb3\xd0\xb0\xd0\xbc\xd0\xb8'), (3, b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xb8\xd0\xbc \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xbc'), (4, b'\xd0\x9f\xd0\xbe \xd1\x81\xd1\x87\xd0\xb5\xd1\x82\xd1\x83(\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x8e\xd1\x80 \xd0\xbb\xd0\xb8\xd1\x86)')]),
        ),
        migrations.AlterField(
            model_name='clients',
            name='private_stock',
            field=models.FloatField(default=0, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='title',
            field=models.CharField(max_length=256, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='unpaid_orders',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd0\xbd\xd0\xb5\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='unpaid_sum',
            field=models.FloatField(default=0, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb4\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='comments',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='map',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd0\xb8\xd0\xbf\xd1\x82 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='zip',
            field=models.CharField(max_length=12, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb8\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='map',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd0\xb8\xd0\xbf\xd1\x82 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='deliveryinfo',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xb3\xd1\x80\xd1\x83\xd0\xb7\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='file',
            field=models.TextField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb', blank=True),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='export1c',
            name='type',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb2\xd1\x8b\xd0\xb3\xd1\x80\xd1\x83\xd0\xb7\xd0\xba\xd0\xb8', choices=[(0, b'Goods'), (1, b'Orders')]),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='forsuppliers',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='cost',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='delivery_time',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='shop.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='meassure',
            field=models.CharField(default=b'\xd1\x88\xd1\x82.', max_length=64, verbose_name=b'\xd0\x95\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='partnumber',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x90\xd1\x80\xd1\x82\xd0\xb8\xd0\xba\xd1\x83\xd0\xbb', blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price_list',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb9\xd1\x81-\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x8b', blank=True, to='shop.PriceList', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='remainder',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9e\xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd0\xbe\xd0\xba \xd0\xbd\xd0\xb0 \xd1\x81\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='reserved',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x97\xd0\xb0\xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='show_on_index',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbd\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x90\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f', blank=True, to='shop.Stock', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='stock_price',
            field=models.FloatField(default=0.0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xbe \xd0\xb0\xd0\xba\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd1\x89\xd0\xb8\xd0\xba', blank=True, to='shop.Supplier', null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='markup',
            name='developer',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='shop.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='goods_category',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb2', blank=True, to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='markup',
            name='pricelist',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb9\xd1\x81-\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82', blank=True, to='shop.PriceList', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='suppliers',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd1\x89\xd0\xb8\xd0\xba', blank=True, to='shop.Supplier', null=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='title',
            field=models.CharField(max_length=256, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='markup',
            name='value',
            field=models.FloatField(default=0, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbd\xd0\xb0\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods_pn',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x90\xd1\x80\xd0\xba\xd1\x82\xd0\xb8\xd0\xba\xd1\x83\xd0\xbb'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='goods_price',
            field=models.FloatField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb7\xd0\xb0 \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd1\x83'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7', to='shop.Orders'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='total_goods_price',
            field=models.FloatField(verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='client',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82', to='shop.Clients'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='comments',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivery_address',
            field=models.TextField(null=True, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_sum',
            field=models.FloatField(default=0, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payments',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0', choices=[(0, b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xba\xd1\x83\xd1\x80\xd1\x8c\xd0\xb5\xd1\x80\xd1\x83'), (1, b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xbe\xd0\xb9'), (2, b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c\xd0\xb3\xd0\xb0\xd0\xbc\xd0\xb8'), (3, b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xb8\xd0\xbc \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xbc'), (4, b'\xd0\x9f\xd0\xbe \xd1\x81\xd1\x87\xd0\xb5\xd1\x82\xd1\x83(\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xba\xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x8e\xd1\x80 \xd0\xbb\xd0\xb8\xd1\x86)')]),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0', choices=[(0, b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd'), (1, b'\xd0\x92 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb5'), (2, b'\xd0\xa1\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd'), (3, b'\xd0\x9e\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd')]),
        ),
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='image',
            field=models.ImageField(default=None, upload_to=b'uploads', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='url',
            field=models.SlugField(verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbd\xd0\xbe\xd1\x81\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 URL'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xb3\xd1\x80\xd1\x83\xd0\xb7\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='file',
            field=models.FileField(upload_to=b'pricelists', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb'),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd1\x89\xd0\xb8\xd0\xba', to='shop.Supplier'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='developer',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True, to='shop.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='goods_category',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb2', blank=True, to='shop.GoodsCategory', null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='show_on_main_page',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xba\xd0\xb0\xd0\xb7\xd1\x8b\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbd\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.FloatField(default=0, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='bank_data',
            field=models.TextField(verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xbe\xd0\xb2\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb2\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x82\xd1\x8b'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbb\xd0\xb8\xd1\x86\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_email',
            field=models.EmailField(max_length=75, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 email', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_phone',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='fact_address',
            field=models.TextField(verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='law_address',
            field=models.TextField(verbose_name=b'\xd0\xae\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='title',
            field=models.CharField(max_length=256, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
    ]
