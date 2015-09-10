# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20150314_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payments',
            field=models.IntegerField(verbose_name='Метод платежа', default=0, choices=[(0, 'Наличными курьеру'), (1, 'Банковской картой'), (2, 'Электронными деньгами'), (3, 'Банковским переводом'), (4, 'По счету(только для юр лиц)')]),
            preserve_default=True,
        ),
    ]
