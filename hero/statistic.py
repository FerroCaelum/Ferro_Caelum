# coding: utf-8
from django.db import models
from hero.effect_instance import EffectInstance

__author__ = 'episage'

class Statistic(models.Model):
    base = models.BigIntegerField(default=10)
    value = models.BigIntegerField(default=10)
    effects = models.ManyToManyField(EffectInstance)