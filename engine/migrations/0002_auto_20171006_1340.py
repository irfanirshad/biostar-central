# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='log',
            field=models.TextField(default='log'),
        ),
        migrations.AddField(
            model_name='job',
            name='uid',
            field=models.CharField(default='', max_length=32),
        ),
    ]
