# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'film title')),
                ('poster', models.ImageField(upload_to=b'uploads/posters', max_length=255, verbose_name=b'film poster')),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'search date')),
            ],
            options={
                'db_table': 'poster',
                'verbose_name_plural': 'posters',
            },
        ),
    ]
