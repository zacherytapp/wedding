# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='button_link',
            field=models.URLField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='link_title',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
