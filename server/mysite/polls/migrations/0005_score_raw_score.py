# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_institution_institution_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='raw_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
