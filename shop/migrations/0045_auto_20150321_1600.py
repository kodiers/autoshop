# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0044_basket_private_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', ckeditor.fields.RichTextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('cost', models.FloatField(null=True, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True)),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0442\u043e\u0434 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438',
                'verbose_name_plural': '\u041c\u0435\u0442\u043e\u0434\u044b \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4 \xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True, to='shop.DeliveryMethods', null=True),
            preserve_default=True,
        ),
    ]
