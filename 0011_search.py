# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_call_comment_question_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('font_file', models.FileField(upload_to='')),
            ],
        ),
    ]
