# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-13 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0013_auto_20200413_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='min_price',
            field=models.IntegerField(default=models.IntegerField()),
        ),
    ]
