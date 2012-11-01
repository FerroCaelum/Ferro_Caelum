# coding: utf-8
from django.db import models

class Ability(models.Model):
    """Reprezentuje zdolność aktywowaną przez bohatera podczas walki."""
    name = models.CharField(max_length=50)
    last = models.PositiveSmallIntegerField()
    time = models.PositiveSmallIntegerField() #ilosc tur trwania ability

    #bonus umiejetnosci w procentach, 100% - bez zmian

    melee_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak wręcz
    range_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak dystansowy
    programming = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #programowanie
    web_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #używanie sieci
    antivirus_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #obrona antywirusowa
    dodge = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #uniki
    quick_move = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #szybkie poruszanie się
    detection_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #ukrywanie się
    health_points = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0)
    #Staystyki nieobsługiwana przez getter:
    virus_resist = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0)
    hiding = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) # + kamuflarz ?
    detection = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) # + detektor ?
    movement_speed = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0)
    #Trzeba nad tym podyskutować
    weapon_switching_speed_uno = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0)

    def is_field(self):
        return False
