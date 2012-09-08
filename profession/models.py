# coding: utf-8

from django.db import models

class Profession(models.Model):
    power_cost = models.PositiveIntegerField(default=30) #moc
    resistance_cost = models.PositiveIntegerField(default=30) #wytrzymałość
    dexterity_cost = models.PositiveIntegerField(default=30) #zręczność
    perception_cost = models.PositiveIntegerField(default=30) #percepcja
    intelligence_cost = models.PositiveIntegerField(default=30) #inteligencja
    web_cost = models.PositiveIntegerField(default=30) #sieć
    artifice_cost = models.PositiveIntegerField(default=30) #spryt
    #umiejętności
    detection_cost = models.PositiveIntegerField(default=10) #detekcja
    hide_cost = models.PositiveIntegerField(default=10) #kamuflaż
    trade_cost = models.PositiveIntegerField(default=10) #handel