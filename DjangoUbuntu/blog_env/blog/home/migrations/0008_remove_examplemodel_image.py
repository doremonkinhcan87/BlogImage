# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20151227_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examplemodel',
            name='image',
        ),
    ]
