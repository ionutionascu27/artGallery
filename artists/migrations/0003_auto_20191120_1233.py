# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-20 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20191107_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='artist',
        ),
    ]
