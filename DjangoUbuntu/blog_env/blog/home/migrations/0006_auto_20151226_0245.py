# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 02:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_examplemodel_image_char'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examplemodel',
            old_name='image',
            new_name='model_pic',
        ),
    ]