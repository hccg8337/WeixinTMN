from __future__ import unicode_literals

from django.db import models

from WeixinTMN.models import Type


class NodeIcon(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200)


class Node(models.Model):
    DEFAULT = {
        'notifytime': 5,
    }

    TYPE = (
        (1, 'template'),
        (2, 'instance'),
    )

    STATE = (
        (1, 'nouse'),
        (2, 'unfinished'),
        (3, 'broken'),
        (4, 'done')
    )

    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=TYPE)
    deadline = models.DateTimeField(null=True)
    notifytime = models.IntegerField(default=DEFAULT['notifytime'])
    comments = models.TextField(default='')
    gameid = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='game2node', null=True)
    state = models.IntegerField(choices=STATE, default=2)
    documents = models.ManyToManyField('document.Document', related_name='node2document')
    nodeiconid = models.ForeignKey('NodeIcon', on_delete=models.SET_NULL, related_name='node2nodeicon')

    class Meta:
        ordering = ['id']


"""class NodeRelationship(models.Model):
    nodeid = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='childnode')
    parentnodeid = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='parentnode', null=True)

    class Meta:
        ordering = ['nodeid']"""


class NodesLine(models.Model):
    STATE = (
        (1, 'normal'),
        (2, 'broken'),
    )

    prevnodeid = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='lineprevnode')
    nextnodeid = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='linenextnode')
    state = models.IntegerField(choices=STATE, default=1)

    class Meta:
        ordering = ['prevnodeid']


class NodeState(object):
    NOUSE = 1
    UNFINISHED = 2
    BROKEN = 3
    DONE = 4


class NodeType(Type):
    pass