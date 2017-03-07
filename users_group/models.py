from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UsersGroup(models.Model):
    STATE = (
        (1, 'used'),
        (2, 'forbidden'),
    )

    name = models.CharField(max_length=50, unique=True)
    comments = models.CharField(max_length=200, default='')
    state = models.IntegerField(choices=STATE, default=1)
    nodes = models.ManyToManyField('node.Node', related_name='usersgroup2node')

    class Meta:
        ordering = ['name']


class UsersGroupState(object):
    USED = 1
    FORBIDDEN = 2