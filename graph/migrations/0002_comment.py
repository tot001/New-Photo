# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('pinglun', models.CharField(max_length=200)),
                ('like', models.IntegerField()),
            ],
        ),
    ]