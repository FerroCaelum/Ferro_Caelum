# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator

class Profession(models.Model):
    hp_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=10.0) #punkty życia
    #atrybuty
    power_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #moc
    resistance_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #wytrzymałość
    dexterity_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #zręczność
    perception_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #percepcja
    intelligence_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #inteligencja
    web_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #sieć
    artifice_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #spryt
    #umiejętności
    detection_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #detekcja
    hide_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #kamuflaż
    trade_progres = models.DecimalField(max_digits=6, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #handel