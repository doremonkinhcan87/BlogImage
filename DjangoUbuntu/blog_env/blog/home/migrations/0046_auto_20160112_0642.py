# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 06:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_auto_20160112_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='document',
        ),
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AlterField(
            model_name='document',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Users'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
