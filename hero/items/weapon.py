# coding: utf-8
from django.db import models
from hero.items.item import Item
from hero.statistic import Statistic

__author__ = 'episage'

class Weapon(Item):
    speed = models.ForeignKey(Statistic, related_name="speed")
    hit_bonus = models.ForeignKey(Statistic, related_name="hit_bonus")
    piercing_dmg = models.ForeignKey(Statistic, related_name="piercing_dmg")
    energetic_dmg = models.ForeignKey(Statistic, related_name="energetic_dmg")
    critical = models.ForeignKey(Statistic, related_name="critical")