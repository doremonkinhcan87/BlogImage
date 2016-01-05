# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=200)),
                ('page_slug', models.SlugField()),
                ('published_date', models.DateTimeField(verbose_name='date published')),
                ('page_content', models.TextField()),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]
