# coding: utf-8

from django.db import models


class BloodLine(models.Model):
    name = models.CharField(max_length=50) #blood line name
    power = models.PositiveIntegerField(default=8) #moc
    resistance = models.PositiveIntegerField(default=8) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=8) #zręczność
    perception = models.PositiveIntegerField(default=8) #percepcja
    intelligence = models.PositiveIntegerField(default=8) #inteligencja
    web = models.PositiveIntegerField(default=8) #sieć
    artifice = models.PositiveIntegerField(default=8) #spryt
    #podstawowe
    hp = models.PositiveIntegerField(default=10) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    speed = models.PositiveIntegerField(default=100) #prędkość
    #umiejętności
    detection = models.PositiveIntegerField(default=0) #detekcja
    hide = models.PositiveIntegerField(default=0) #kamuflaż
    trade = models.PositiveIntegerField(default=0) #handel
    def __unicode__(self):
        return self.name    