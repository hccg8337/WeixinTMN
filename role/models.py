from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Role(models.Model):
    STATE = (
        (1, 'used'),
        (2, 'forbidden'),
    )

    name = models.CharField(max_length=50, unique=True)
    cnname = models.CharField(max_length=50, unique=True, null=True)
    comments = models.CharField(max_length=200, default='')
    state = models.IntegerField(choices=STATE, default=1)
    actions = models.ManyToManyField('action.Action', related_name='role2action')

    class Meta:
        ordering = ['name']


class RoleType(object):
    pass