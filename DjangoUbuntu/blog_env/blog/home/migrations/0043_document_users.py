# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_remove_document_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.Users'),
            preserve_default=False,
        ),
    ]
