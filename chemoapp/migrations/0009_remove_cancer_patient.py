# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-13 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemoapp', '0008_auto_20190713_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancer',
            name='patient',
        ),
    ]
