# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0003_auto_20180930_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
