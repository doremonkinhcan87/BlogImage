# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_document_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
