# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['no']},
        ),
        migrations.AlterField(
            model_name='module',
            name='no',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
