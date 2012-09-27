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
    
    def get_statistic(self, number):
        if number == 1: 
            return self.power
        if number == 2: 
            return self.resistance
        if number == 3: 
            return self.dexterity
        if number == 4: 
            return self.perception
        if number == 5: 
            return self.intelligence
        if number == 6: 
            return self.web
        if number == 7: 
            return self.artifice
        if number == 8: 
            return self.hp
        if number == 9: 
            return self.ap
        if number == 10: 
            return self.speed
        if number == 11: 
            return self.hide
        if number == 12: 
            return self.detection
        if number == 13: 
            return self.trade
        
    def get_updated_statistic(self, number):
        talents = Talent.objects.filter(hero__pk=self.pk)
        talents_set_sum = set()
        sum = 0
        talents_set_multi = set()
        multi = 100
        
        for t in talents:
            talents_set_sum.add(EffectOfTalent.objects.filter(talent__pk = t.pk).filter(where_works = number).filter(variable = number).filter(percent = False))
        for effects_set in talents_set_sum:
            for e in effects_set:
                sum+=e.value   
                  
        for t in talents:
            talents_set_multi.add(EffectOfTalent.objects.filter(talent__pk = t.pk).filter(where_works = number).filter(variable = number).filter(percent = True))
        for effects_set in talents_set_multi:
            for e in effects_set:
                multi+=e.value   
        return 0.01*multi*(self.get_updated_statistic(number)+sum)        
    
    def get_updated_power(self):
#        talents = Talent.objects.filter(hero__pk=self.pk)
#        talents_set_sum = set()
#        sum = 0
#        talents_set_multi = set()
#        multi = 100
#        
#        for t in talents:
#            talents_set_sum.add(EffectOfTalent.objects
#                                .filter(talent__pk=t.pk).filter(where_works=1)
#                                .filter(variable=1).filter(percent=False))
#        for _set in talents_set_sum:
#            for e in _set:
#                sum+=e.value   
#                  
#        for t in talents:
#            talents_set_multi.add(EffectOfTalent.objects
#                                  .filter(talent__pk=t.pk).filter(where_works=1)
#                                  .filter(variable=1).filter(percent=True))
#        for _set in talents_set_multi:
#            for e in _set:
#                multi+=e.value   
#        return 0.01*multi*(self.power+sum)
        return self.get_updated_statistic(1)
    
    def __unicode__(self):
        return self.name