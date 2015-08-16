# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20150815_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='display_order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='visibility',
            field=models.CharField(default=b'Unpublished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpublished', b'Unpublished')]),
        ),
    ]
