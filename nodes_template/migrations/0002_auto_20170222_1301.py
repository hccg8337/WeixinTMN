# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0002_auto_20170222_1301'),
        ('nodes_template', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodestemplate',
            name='nodeids',
        ),
        migrations.AddField(
            model_name='nodestemplate',
            name='nodeids',
            field=models.ManyToManyField(related_name='nodestemplate2node', to='node.Node'),
        ),
    ]
