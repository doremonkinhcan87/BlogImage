# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_document_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='document',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
