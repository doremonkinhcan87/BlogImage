# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160107_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
