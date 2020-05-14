# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-07 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0003_painting_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='media',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='paintings.Media'),
        ),
        migrations.AddField(
            model_name='painting',
            name='trend',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='paintings.Trend'),
        ),
    ]