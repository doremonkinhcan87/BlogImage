# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20160112_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='users',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.Users'),
        ),
    ]