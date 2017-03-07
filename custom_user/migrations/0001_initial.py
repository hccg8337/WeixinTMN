# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_group', '0001_initial'),
        ('action', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unionid', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(max_length=100, null=True)),
                ('openid', models.CharField(max_length=100, null=True)),
                ('actions', models.ManyToManyField(related_name='user2action', to='action.Action')),
                ('usersgroup', models.ManyToManyField(related_name='user2usersgroup', to='users_group.UsersGroup')),
            ],
            options={
                'ordering': ['nickname'],
            },
        ),
    ]
