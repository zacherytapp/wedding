# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20150819_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('display_order', models.IntegerField()),
                ('visibility', models.CharField(default=b'Unpusblished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpusblished', b'Unpusblished')])),
                ('title', models.CharField(max_length=200)),
                ('timeline_description', ckeditor.fields.RichTextField()),
                ('link_title', models.CharField(max_length=200)),
                ('button_link', models.URLField(max_length=500)),
                ('show_button', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
