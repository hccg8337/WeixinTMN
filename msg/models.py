from __future__ import unicode_literals

from django.db import models


class MsgStructure(models.Model):
    content = models.TextField(default='')
    no = models.CharField(max_length=50)

    class Meta:
        ordering = ['no']


class Msg(models.Model):
    content = models.TextField(default='')
    createtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createtime']


class MsgState(models.Model):
    state = (
        (1, 'notread'),
        (2, 'read'),
    )

    msgid = models.ForeignKey('msg.Msg', on_delete=models.CASCADE, related_name='msgstate2msg')
    userid = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE, related_name='msgstate2user')
    state = models.IntegerField(choices=state, default=1)


class MsgStateType(object):
    NOTREAD = 1
    READ = 2


class MsgStructureAction(object):
    NODE_STATE_CHANGE = '001'
    GIVE_NODE_TO_USER = '002'
    NODE_OVERTIME = '003'
    NODE_NOTIFY = '004'
    GIVE_GAME_TO_USER = '005'
    CANCELL_NODE_FROM_USER = '006'