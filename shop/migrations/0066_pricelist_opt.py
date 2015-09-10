# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0065_auto_20150421_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelist',
            name='opt',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb9\xd1\x81-\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbe\xd0\xbf\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd1\x85 \xd0\xbf\xd0\xbe\xd0\xba\xd1\x83\xd0\xbf\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb9'),
            preserve_default=True,
        ),
    ]
