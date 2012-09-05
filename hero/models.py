# coding: utf-8

from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    lvl = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    energy = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=20.0)
    gold = models.DecimalField(max_digits=20, decimal_places=2, default=0.0) #stan konta
    #atrybuty
    power = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #moc
    resistance = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #wytrzymałość
    dexterity = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #zręczność
    perception = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #percepcja
    intelligence = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #inteligencja
    web = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #sieć
    artifice = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #spryt
    #statystyki główne
    hp = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=10.0) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    speed = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=1.0) #prędkość
    #umiejętności
    detection = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #detekcja
    hide = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #kamuflaż
    trade = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #handel
    #wyćwiczenie
    #>Bojowe
    melee_attack = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak wręcz
    range_attack = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak dystansowy
    programming = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #programowanie
    web_use = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #używanie sieci
    antivirus_use = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #obrona antywirusowa
    dodge = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #uniki
    quick_move = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(1.0)], default=1.0) #szybkie poruszanie się
    #>Umiejętności
    detection_use = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #ukrywanie się
    trade_use = models.DecimalField(max_digits=15, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #handlowanie