# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='center_lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zone',
            name='center_lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
