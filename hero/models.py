# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator

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

class Hero(models.Model):
    name = models.CharField(max_length=60)
    lvl = models.PositiveIntegerField(default=1)
    lvl_points = models.PositiveIntegerField(default=100)
    blood_line = models.ForeignKey(BloodLine)   
    profession = models.ForeignKey(Profession)
    experience = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=20)
    gold = models.DecimalField(max_digits=20, decimal_places=2, default=0.0) #stan konta
    #atrybuty
    power = models.PositiveIntegerField(default=1) #moc
    resistance = models.PositiveIntegerField(default=1) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1) #zręczność
    perception = models.PositiveIntegerField(default=1) #percepcja
    intelligence = models.PositiveIntegerField(default=1) #inteligencja
    web = models.PositiveIntegerField(default=1) #sieć
    artifice = models.PositiveIntegerField(default=1) #spryt
    #statystyki główne
    hp = models.PositiveIntegerField(default=10) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    speed = models.PositiveIntegerField(default=100) #prędkość
    #umiejętności
    detection = models.PositiveIntegerField(default=0) #detekcja
    hide = models.PositiveIntegerField(default=0) #kamuflaż
    trade = models.PositiveIntegerField(default=0) #handel
    #wyćwiczenie
    #>Bojowe
    melee_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak wręcz
    range_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak dystansowy
    programming = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #programowanie
    web_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #używanie sieci
    antivirus_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #obrona antywirusowa
    dodge = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #uniki
    quick_move = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #szybkie poruszanie się
    #>Umiejętności
    detection_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #ukrywanie się
    trade_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #handlowanie 

class Ability(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    abilities_requirements = models.ManyToManyField('self', through='Ability_requierment', 
                                                    symmetrical=False, related_name='requires')
    def add_required_ability(self, ability):
        Ability_requierment, created = Ability_requierment.objects.get_or_create(
            ability_require=self,
            ability_required=person)
        return relationship
    def remove_required_ability(self, ability):
        Ability_requierment.objects.filter(
             ability_require=self,
             ability_required=ability).delete()
        return
   
class Ability_requierment(models.Model):
    ability_require = models.ForeignKey(Ability, related_name='require')
    ability_required = models.ForeignKey(Ability, related_name='required')
    
class Stats_requierment(models.Model):
    ability = models.ForeignKey(Ability)
    stats_requirement = models.PositiveIntegerField()
    
class Effect(models.Model): 
    ability = models.ForeignKey(Ability)
    type = models.SmallIntegerField()
    effect = models.PositiveIntegerField()
    hero = models.ManyToManyField(Hero)
       
class BloodLineAbility(models.Model):
    blood_line = models.ForeignKey(BloodLine)
    ability = models.OneToOneField(Ability)
