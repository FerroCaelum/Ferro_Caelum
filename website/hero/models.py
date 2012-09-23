# coding: utf-8

from django.db import models

"""
Wszystkie statystyki odnoszące się do bohatera powinne być w 1 tabeli.

Większość wartości defaultowych nie będzie używanych z uwagi na fakt, że statsy każdego bohatera będą przypisywane przy
rejestracji w zależności od wyboru linii krwi, czy innych "rzeczy".

Poprawiłem angielskie nazwy.
"""

class Owner(models.Model):
    max_load = models.DecimalField(max_digits=10, decimal_places=2,
        default=80) #+funkcja agregująca obecny ładunek (nie umiem)
    name = models.CharField(
        max_length=50
    ) # http://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields

    def __unicode__(self):
        return u'%s' % self.name


class Hero(Owner):
    lvl = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=20)
    hp = models.PositiveIntegerField(default=10) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    #atrybuty
    power = models.PositiveIntegerField(default=1) #moc
    resistance = models.PositiveIntegerField(default=1.0) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1.0) #zręczność
    perception = models.PositiveIntegerField(default=1.0) #percepcja
    intelligence = models.PositiveIntegerField(default=1.0) #inteligencja
    web = models.PositiveIntegerField(default=1.0) #sieć
    artifice = models.PositiveIntegerField(default=1.0) #spryt

    #statystyki główne
    #CanTakeDmg
    #CanGiveDmg
    speed = models.PositiveIntegerField(default=5) #prędkość http://pl.wikipedia.org/wiki/Kilometr_na_godzin%C4%99

    #statystyki bojowe
    hiding = models.PositiveIntegerField(default=0.0) #ukrywanie
    detection = models.PositiveIntegerField(default=0.0) #detekcja

    #umiejętności walki
    melee_attack = models.PositiveIntegerField(default=0.0) #atak wręcz
    range_attack = models.PositiveIntegerField(default=0.0) #atak dystansowy
    programming = models.PositiveIntegerField(default=0.0) #programowanie
    web_use = models.PositiveIntegerField(default=0.0) #używanie sieci
    antivirus_use = models.PositiveIntegerField(default=0.0) #obrona antywirusowa
    dodge = models.PositiveIntegerField(default=0.0) #uniki
    hiding_use = models.PositiveIntegerField(default=0.0) #ukrywanie się
    detection_use = models.PositiveIntegerField(default=0.0) #wykrywanie
    quick_move = models.PositiveIntegerField(default=1.0) #szybkie poruszanie się

    def Attack(self, hero):
        pass


