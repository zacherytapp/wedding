# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20150815_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='visibility',
            field=models.CharField(default=b'Unpusblished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpusblished', b'Unpusblished')]),
        ),
    ]
