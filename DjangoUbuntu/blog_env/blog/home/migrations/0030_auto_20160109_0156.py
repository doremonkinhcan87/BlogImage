# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20160108_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
