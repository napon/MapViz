# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170225_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='norm_count',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
