from __future__ import unicode_literals

from django.db import models


class Config(models.Model):
    name = models.CharField(max_length=50)
    value = models.TextField(default='')

    class Meta:
        ordering = ['name']