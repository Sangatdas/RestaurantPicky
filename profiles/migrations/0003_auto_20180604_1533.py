# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-04 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180604_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='following',
            new_name='followers',
        ),
    ]
