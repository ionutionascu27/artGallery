# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-23 15:08
from __future__ import unicode_literals

import auction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_auto_20200123_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(),
        ),
    ]
