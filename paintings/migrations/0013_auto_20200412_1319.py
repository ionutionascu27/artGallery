# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-12 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0012_auto_20200408_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='painting',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
