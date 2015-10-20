# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('display_order', models.IntegerField()),
                ('visibility', models.CharField(default=b'Unpusblished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpusblished', b'Unpusblished')])),
                ('title', models.CharField(max_length=50)),
                ('alt_text', models.CharField(max_length=200)),
                ('registry_image', models.ImageField(upload_to=b'')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
