# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
