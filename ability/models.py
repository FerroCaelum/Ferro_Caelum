# coding: utf-8
from django.db import models

class Ability(models.Model):
    """Reprezentuje zdolność aktywowaną przez bohatera podczas walki."""
    name = models.CharField(max_length=50)
    last = models.PositiveSmallIntegerField()
    time = models.PositiveSmallIntegerField() #ilosc tur trwania ability


    melee_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak wręcz
    range_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak dystansowy
    programming = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #programowanie
    web_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #używanie sieci
    antivirus_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #obrona antywirusowa
    dodge = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #uniki
    quick_move = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #szybkie poruszanie się
    detection_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #ukrywanie się
    health_points = hp + resistance * 2
    #Staystyki nieobsługiwana przez getter:
    virus_resist = antyvirus_use + 0.5 * resistance + 0.5 * intelligence
    hiding = hide_use + dexternity # + kamuflarz ?
    detection = detection_use + perception # + detektor ?
    movement_speed = quick_move + 0.5 * power
    #Trzeba nad tym podyskutować
    weapon_switching_speed_uno = 90001

    def is_field(self):
        return false
