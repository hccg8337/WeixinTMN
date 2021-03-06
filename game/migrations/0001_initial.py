# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nodes_template', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('workstarttime', models.DateTimeField()),
                ('workendtime', models.DateTimeField()),
                ('workextratime', models.IntegerField(default=0)),
                ('type', models.IntegerField(choices=[(1, 'template'), (2, 'instance')])),
                ('place', models.CharField(default='', max_length=50)),
                ('gamestarttime', models.DateTimeField()),
                ('comments', models.CharField(max_length=200)),
                ('state', models.IntegerField(choices=[(1, 'default'), (2, 'done'), (3, 'cancelled')])),
            ],
            options={
                'ordering': ['workstarttime'],
            },
        ),
        migrations.CreateModel(
            name='Game2NodesTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('nodestemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodes_template.NodesTemplate')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='game2nodestemplate',
            unique_together=set([('gameid', 'nodestemplate')]),
        ),
    ]
