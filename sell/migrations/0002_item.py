# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 11:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='neighimage/')),
                ('description', models.CharField(default='My hood!!!', max_length=300)),
                ('price', models.IntegerField(default='$ 0.0')),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userholder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
