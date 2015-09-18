# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('display_order', models.IntegerField()),
                ('visibility', models.CharField(default=b'Unpusblished', max_length=20, choices=[(b'Published', b'Published'), (b'Unpusblished', b'Unpusblished')])),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('alt_text', models.CharField(max_length=200)),
                ('role', models.CharField(default=b'Bride', max_length=20, choices=[(b'Bride', b'Bride'), (b'Groom', b'Groom'), (b'Groomsman', b'Groomsman'), (b'Bridesmaid', b'Bridesmaid'), (b'Best Man', b'Best Man'), (b'Maid of Honor', b'Maid of Honor'), (b'Matron of Honor', b'Matron of Honor'), (b'Usher', b'Usher'), (b'Officiant', b'Officiant')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
