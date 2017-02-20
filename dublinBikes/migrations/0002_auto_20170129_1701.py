# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-29 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBikes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='dateTaken',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='availability',
            name='name',
            field=models.CharField(default=' ', max_length=100, null=True),
        ),
    ]
