# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_auto_20181024_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]