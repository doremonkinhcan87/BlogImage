# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 04:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]