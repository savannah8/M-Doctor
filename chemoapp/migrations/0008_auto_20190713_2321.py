# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-13 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemoapp', '0007_auto_20190713_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancer',
            name='illness',
            field=models.CharField(choices=[('Cervical Cancer', 'Cervical Cancer')], max_length=50),
        ),
    ]
