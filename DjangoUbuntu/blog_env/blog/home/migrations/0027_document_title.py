# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
