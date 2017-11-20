# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-20 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomalloc', '0006_auto_20171120_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reason',
            field=models.CharField(default='Study', help_text='Reason summarized', max_length=200),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(help_text='Max capacity of room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='tech',
            field=models.TextField(help_text='Technology is room'),
        ),
    ]