# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20170209_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='usersgroup',
            new_name='usersgroups',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unionid',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
