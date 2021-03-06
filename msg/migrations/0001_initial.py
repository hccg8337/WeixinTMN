# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0003_auto_20170222_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-createtime'],
            },
        ),
        migrations.CreateModel(
            name='MsgState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'notread'), (2, 'read')], default=1)),
                ('msgid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgstate2msg', to='msg.Msg')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgstate2user', to='custom_user.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='MsgStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('no', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['no'],
            },
        ),
    ]
