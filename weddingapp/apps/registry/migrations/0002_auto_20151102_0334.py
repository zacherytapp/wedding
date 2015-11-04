# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='visibility',
            field=models.CharField(default=b'Unpublished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpublished', b'Unpublished')]),
        ),
    ]
