# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160114_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='document',
            name='subtitle',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='document',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]