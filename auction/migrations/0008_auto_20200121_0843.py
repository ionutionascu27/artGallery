# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-21 08:43
from __future__ import unicode_literals

import auction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_auto_20200116_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='increment',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='start_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='winner_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(),
        ),
    ]
