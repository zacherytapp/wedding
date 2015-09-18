# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_auto_20150823_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='timeline_date',
            field=models.CharField(default='Jan 1', max_length=50),
            preserve_default=False,
        ),
    ]
