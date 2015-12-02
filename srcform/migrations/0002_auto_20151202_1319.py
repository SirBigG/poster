# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='poster',
            field=models.ImageField(upload_to=b'uploads/posters', verbose_name=b'film poster'),
        ),
    ]
