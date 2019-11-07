# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-06 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='size',
            field=models.CharField(choices=[('', '---------'), ('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], default='', max_length=24),
        ),
    ]