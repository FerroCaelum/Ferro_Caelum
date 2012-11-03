# coding: utf-8
from django.db import models

__author__ = 'episage'

class Effect(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    priority= models.IntegerField(default=0)

    def __unicode__(self):
        return u'Effect %s' % self.name