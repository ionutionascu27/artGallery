# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-08 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0011_auto_20200408_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='painting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='paintings.Painting'),
        ),
    ]
