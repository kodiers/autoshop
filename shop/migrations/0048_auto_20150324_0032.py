# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_auto_20150322_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsMethods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.TextField(max_length=128, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0442\u043e\u0434 \u043f\u043b\u0430\u0442\u0435\u0436\u0430',
                'verbose_name_plural': '\u041c\u0435\u0442\u043e\u0434\u044b \u043f\u043b\u0430\u0442\u0435\u0436\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payments',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb4 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0', to='shop.PaymentsMethods'),
        ),
    ]
