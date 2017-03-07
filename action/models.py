# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Action(models.Model):
    STATE = (
        (1, 'used'),
        (2, 'forbidden'),
    )

    no = models.CharField(max_length=20)
    name = models.CharField(max_length=50, default='')
    cnname = models.CharField(max_length=50, default='')
    comments = models.CharField(max_length=200, default='')
    state = models.IntegerField(choices=STATE,default=1)
    moduleid = models.ForeignKey('module.Module', on_delete=models.CASCADE)

    class Meta:
        ordering = ['no']


class ActionNoId(object):
    pass



