from __future__ import unicode_literals

from django.db import models



class Module(models.Model):
    no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50, default='')
    cnname = models.CharField(max_length=50, default='')
    comments = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ['no']
