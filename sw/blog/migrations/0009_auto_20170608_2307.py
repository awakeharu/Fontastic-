# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170608_2215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Call',
        ),
    ]