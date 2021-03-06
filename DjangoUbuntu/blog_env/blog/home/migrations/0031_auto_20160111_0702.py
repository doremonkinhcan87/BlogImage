# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20160109_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firt_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
                ('email', models.CharField(default='', max_length=256)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelTable(
            name='document',
            table='document',
        ),
    ]
