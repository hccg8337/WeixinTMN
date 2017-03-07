from __future__ import unicode_literals

from django.db import models

from WeixinTMN.models import Type


class Game(models.Model):
    TYPE = (
        (1, 'template'),
        (2, 'instance'),
    )

    STATE = (
        (1, 'default'),
        (2, 'done'),
        (3, 'cancelled'),
    )

    name = models.CharField(max_length=50)
    workstarttime = models.DateTimeField()
    workendtime = models.DateTimeField()
    workextratime = models.IntegerField(default=0)
    type = models.IntegerField(choices=TYPE)
    place = models.CharField(max_length=50, default='')
    gamestarttime = models.DateTimeField()
    comments = models.CharField(max_length=200, default='')
    state = models.IntegerField(choices=STATE, default=1)
    nodestemplateid = models.ForeignKey('nodes_template.NodesTemplate', on_delete=models.CASCADE, null=True)
    tops = models.CharField(max_length=200)

    class Meta:
        ordering = ['workstarttime']


class GameState(object):
    DEFAULT = Game.STATE[0][0]
    DONE = Game.STATE[1][0]
    CANCELLED = Game.STATE[2][0]
    EMPTY = 4
    NOTSTART = 5
    BROKEN = 6
    OVERTIME = 7
    PROCESSING = 8


class GameType(Type):
    pass


class GamePlace(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name']