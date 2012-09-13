# coding: utf-8

from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=50) # nazwa profesji
    power_cost = models.PositiveIntegerField(default=30) # koszt wykupu punktu moc w punktach awansu
    resistance_cost = models.PositiveIntegerField(default=30) # wykupu punktu wytrzymałości w punktach awansu
    dexterity_cost = models.PositiveIntegerField(default=30) # wykupu punktu zręczności w punktach awansu
    perception_cost = models.PositiveIntegerField(default=30) # wykupu punktu percepcji w punktach awansu
    intelligence_cost = models.PositiveIntegerField(default=30) # wykupu punktu inteligencji w punktach awansu
    web_cost = models.PositiveIntegerField(default=30) # wykupu punktu sieci w punktach awansu
    artifice_cost = models.PositiveIntegerField(default=30) # wykupu punktu sprytu w punktach awansu
    #umiejętności
    detection_cost = models.PositiveIntegerField(default=10) # wykupu punktu detekcji w punktach awansu
    hide_cost = models.PositiveIntegerField(default=10) # wykupu punktu kamuflażu w punktach awansu
    trade_cost = models.PositiveIntegerField(default=10) # wykupu punktu handelu w punktach awansu
    def __unicode__(self):
        return self.name