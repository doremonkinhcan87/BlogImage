# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20160112_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='firt_name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
