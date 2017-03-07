from __future__ import unicode_literals

from django.db import models


class Log(models.Model):
    userid = models.ForeignKey('custom_user.CustomUser', on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now_add=True)
    objectid = models.IntegerField()
    actionid = models.ForeignKey('action.Action', on_delete=models.CASCADE)
    detail = models.TextField(default='')

    class Meta:
        ordering = ['-createtime']