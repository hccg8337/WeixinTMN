# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class DocumentType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']


class Document(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200)
    documenttypeid = models.ForeignKey('DocumentType', on_delete=models.CASCADE, related_name='document2documenttype')
    hashcode = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ['name']




