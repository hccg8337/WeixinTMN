from __future__ import unicode_literals

from django.db import models


class CustomUser(models.Model):
    unionid = models.CharField(max_length=100, null=True, unique=True)
    nickname = models.CharField(max_length=50)
    userid = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    openid = models.CharField(max_length=100, null=True)
    roles = models.ManyToManyField('role.Role', related_name='user2role')
    actions = models.ManyToManyField('action.Action', related_name='user2action')
    games = models.ManyToManyField('game.Game', related_name='user2game')
    nodes = models.ManyToManyField('node.Node', related_name='user2node')
    usersgroups = models.ManyToManyField('users_group.UsersGroup', related_name='user2usersgroup')

    class Meta:
        ordering = ['nickname']


class SessionUser(object):
    SESSION_KEY = 'userid'

    def __init__(self, userid):
        self.userid = userid