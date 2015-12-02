# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcform', '0002_auto_20151202_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='title',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'film title'),
        ),
    ]
