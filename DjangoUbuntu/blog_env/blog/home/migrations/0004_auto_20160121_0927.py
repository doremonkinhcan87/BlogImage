# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_users_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(default='user', max_length=256),
        ),
    ]
