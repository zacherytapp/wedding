# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('message', models.TextField(max_length=5000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
