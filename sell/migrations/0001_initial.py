# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Fashion & Style', 'FASHION & STYLE'), ('Cars & Property', 'CARS & PROPERTY'), ('Electronics & Mobiles', 'ELECTRONICS & MOBILES'), ('Home & Living', 'HOME & LIVING'), ('Others', 'Others')], default='Fashion & Style', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='neighimage/')),
                ('description', models.CharField(max_length=300)),
                ('price', models.IntegerField(default='$ 0.0')),
                ('category', models.CharField(max_length=300)),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_time'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='profile/')),
                ('pub_date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
