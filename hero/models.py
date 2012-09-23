# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator
from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent
from effect.models import *
  
class Owner(models.Model):
    max_load = models.DecimalField(max_digits=10, decimal_places=2,
        default=80) #+funkcja agregująca obecny ładunek (nie umiem)
    name = models.CharField(
        max_length=50
    ) # http://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields

    def __unicode__(self):
        return u'%s' % self.name  

class Hero(Owner):
    name = models.CharField(max_length=60)
    lvl = models.PositiveIntegerField(default=1)
    lvl_points = models.PositiveIntegerField(default=100)
    blood_line = models.ForeignKey(BloodLine)   
    profession = models.ForeignKey(Profession)
    experience = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=20)
    energy_regeneration = models.PositiveIntegerField(default=20)
    gold = models.DecimalField(max_digits=20, decimal_places=2, default=0.0) #stan konta
    talent = models.ManyToManyField(Talent)
    #atrybuty
    power = models.PositiveIntegerField(default=1) #moc
    resistance = models.PositiveIntegerField(default=1) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1) #sprawność
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
    #wyćwiczenie (doświadczenie)
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
    def get_hero_effects(self):
        talents = Talent.objects.filter(hero__pk=self.pk)
        acumulator=[]
        for t in talents:
            acumulator += EffectOfTalent.objects.filter(talent__pk=t.pk)
        return acumulator
    def get_main_stats_effect(self):
        return self.get_hero_effects().filter(where_works=1)
    def get_updated_power(self):
        effects = self.get_main_stats_effect().filter(variable=1)
        es = effects.filter(percent=False)
        sum = 0
        for effect in es:
            sum+=effect.value     
        em = effects.filter(percent=True)
        multi = 100
        for effect in em:
            multi+=effect.value
        return 0.01*multi*(self.power+sum)
    def print_all_effects(self):
        effect=self.get_hero_effects()
        for e in effect: 
            print e.get_description()
    def get_updated_power(self):
        return 
    def __unicode__(self):
        return self.name