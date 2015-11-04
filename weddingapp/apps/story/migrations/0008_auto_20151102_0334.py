# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_timeline_timeline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='visibility',
            field=models.CharField(default=b'Unpublished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpublished', b'Unpublished')]),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='visibility',
            field=models.CharField(default=b'Unpublished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpublished', b'Unpublished')]),
        ),
    ]
