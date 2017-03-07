from __future__ import unicode_literals

from django.db import models


class GamesTemplate(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gameids = models.ManyToManyField('game.Game', related_name='gamestemplate2game')
    comments = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ['name']


class Date2GamesTemplate(models.Model):
    date = models.DateField()
    gamestemplate = models.ForeignKey('GamesTemplate', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'gamestemplate')
