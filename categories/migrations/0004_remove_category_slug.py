# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-07-22 23:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20190722_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]