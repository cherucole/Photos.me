# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 12:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
    ]
