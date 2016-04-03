# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_auto_20151102_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='registry',
            name='registry_url',
            field=models.URLField(default='URL', max_length=500),
            preserve_default=False,
        ),
    ]
