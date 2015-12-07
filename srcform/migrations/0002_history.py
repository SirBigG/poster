# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100, verbose_name=b'search history')),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'date of search')),
                ('status', models.IntegerField(default=0, verbose_name=b'search_status')),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]
