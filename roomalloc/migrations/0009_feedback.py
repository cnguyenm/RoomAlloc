# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-06 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomalloc', '0008_auto_20171120_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField(max_length=2000)),
            ],
        ),
    ]
