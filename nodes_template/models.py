from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NodesTemplate(models.Model):
    name = models.CharField(max_length=50, unique=True)
    nodeids = models.ManyToManyField('node.Node', related_name='nodestemplate2node')
    tops = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']