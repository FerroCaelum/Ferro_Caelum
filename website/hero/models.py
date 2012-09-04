# coding: utf-8

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

'''
Wszystkie statystyki odnoszące się do bohatera powinne być w 1 tabeli.

Większość wartości defaultowych nie będzie używanych z uwagi na fakt, że statsy każdego bohatera będą przypisywane przy
rejestracji w zależności od wyboru linii krwi, czy innych "rzeczy".

Poprawiłem angielskie nazwy.
'''

class Hero(models.Model):
    name = models.CharField(
        max_length=50) # http://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields
    energy = models.PositiveIntegerField(default=0.0)

    #atrybuty
    power = models.PositiveIntegerField(default=1.0) #moc
    resistance = models.PositiveIntegerField(default=1.0) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1.0) #zręczność
    perception = models.PositiveIntegerField(default=1.0) #percepcja
    intelligence = models.PositiveIntegerField(default=1.0) #inteligencja
    web = models.PositiveIntegerField(default=1.0) #sieć
    artifice = models.PositiveIntegerField(default=1.0) #spryt

    #statystyki główne
    hp = models.PositiveIntegerField(default=10) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
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

    def __unicode__(self):
        return self.name

# sorry ale jak mam to testować w kosoli i robić importy z różnych klas to mnie strzela. dla wygody musze to tu przerzucic na chwile
class Item(models.Model):
    count = models.PositiveIntegerField()
    owner = generic.GenericForeignKey()
    #image=models.ImageField()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return str(self.count) + ' of ' + str(Name.objects.get(item=self))


class Name(models.Model):
    name = models.CharField(max_length=50)
    item = models.ForeignKey(Item)

    def __unicode__(self):
        return self.name


class Weapon(models.Model):
    speed = models.PositiveIntegerField()
    hit_bonus = models.IntegerField()
    piercing_dmg = models.IntegerField()
    energetic_dmg = models.IntegerField()
    critical = models.IntegerField()
    item = models.ForeignKey(Item)


class Armature(models.Model):
    speed_mod = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    camouflage = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class Helmet(models.Model):
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    detector = models.PositiveIntegerField()
    programs_def = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class Program(models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    duration = models.FloatField() # timedelta
    item = models.ForeignKey(Item)


class FieldTech(models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    range_def = models.PositiveIntegerField()
    durability = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class WebTech(models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_dmg = models.PositiveIntegerField()
    strike_dmg = models.PositiveIntegerField()
    piercing_dmg = models.PositiveIntegerField()
    critic = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class SpecialProperties(models.Model):
    item = models.ForeignKey(Item)