# coding: utf-8
from django.db import models
from hero.hero import  Owner



    #
    #class Armature(Item):
    #    speed_mod = models.PositiveIntegerField()
    #    energy_def = models.PositiveIntegerField()
    #    piercing_def = models.PositiveIntegerField()
    #    strike_def = models.PositiveIntegerField()
    #    camouflage = models.PositiveIntegerField()
    #
    #
    #class Helmet(Item):
    #    energy_def = models.PositiveIntegerField()
    #    piercing_def = models.PositiveIntegerField()
    #    strike_def = models.PositiveIntegerField()
    #    detector = models.PositiveIntegerField()
    #    programs_def = models.PositiveIntegerField()
    #
    #
    #class Program(Item):
    #    speed = models.PositiveIntegerField()
    #    pool = models.PositiveIntegerField()
    #    type = models.PositiveIntegerField()
    #    duration = models.FloatField() # timedelta
    #
    #
    #class FieldTech(Item):
    #    speed = models.PositiveIntegerField()
    #    pool = models.PositiveIntegerField()
    #    energy_def = models.PositiveIntegerField()
    #    strike_def = models.PositiveIntegerField()
    #    range_def = models.PositiveIntegerField()
    #    durability = models.PositiveIntegerField()
    #    count = models.PositiveIntegerField()
    #
    #
    #class WebTech(Item):
    #    speed = models.PositiveIntegerField()
    #    pool = models.PositiveIntegerField()
    #    energy_dmg = models.PositiveIntegerField()
    #    strike_dmg = models.PositiveIntegerField()
    #    piercing_dmg = models.PositiveIntegerField()
    #    critic = models.PositiveIntegerField()
    #
    #
    #class SpecialProperties(models.Model):
    #    item = models.ForeignKey(ItemInstance)