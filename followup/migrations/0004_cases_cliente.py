# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0003_auto_20171124_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='cliente',
            field=models.CharField(default='SC', max_length=100),
        ),
    ]
