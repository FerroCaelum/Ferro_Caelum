# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator
import armory.models
from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent
from effect.models import *
  
class Owner(models.Model):
    name = models.CharField(max_length=50)

    max_load = models.DecimalField(max_digits=10, decimal_places=2, default=80)
    load = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def give(self, item, new_owner, count):
        """
        Przekazuje item nowemu właścicielowi.

        :param new_owner: komu przekazać item'y
        :type new_owner: hero.Owner
        :param count: ilość
        :type count: int
        :returns: przekazane item'y
        :rtype: Items
        """

        assert item is armory.models.Item
        assert new_owner is Owner
        assert count is int

        if not item.tradeable: raise u'%s is not tradeable.' % self.name
        itemInstances = armory.models.ItemInstance.objects.filter(owner=self, item=item)
        itemInstancesCount = itemInstances.count()
        if itemInstancesCount <= 0: raise u'%s does not have any of %s.' % self.name, item.name
        if itemInstancesCount > 0: raise u'Server error! Item=%s Owner=%s.' % item.name, self.name
        itemInstance = itemInstances[0]
        ownedCount = itemInstance.count
        if ownedCount < count: raise u'%s cannot give more than they have of %s.' % self.name, item.name
        itemInstance.count -= count
        itemInstance.item.spawn(count, new_owner)

    def __unicode__(self):
        return u'%s' % self.name


class Hero(Owner):
    lvl = models.PositiveIntegerField(default=1)
    lvl_points = models.PositiveIntegerField(default=100)
    blood_line = models.ForeignKey(BloodLine, null=True)
    profession = models.ForeignKey(Profession, null=True)
    experience = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=20)
    energy_regeneration = models.PositiveIntegerField(default=20)
    gold = models.DecimalField(max_digits=20, decimal_places=2, default=0.0) #stan konta
    talents = models.ManyToManyField(Talent, null=True)

    #atrybuty aktualne
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
    
    #statystyki główne bazowe
    hp_base = models.PositiveIntegerField(default=10) #punkty życia
    ap_base = models.PositiveIntegerField(default=100) #punkty akcji
    speed_base = models.PositiveIntegerField(default=100) #prędkość
    
    #umiejętności bazowe
    detection_base = models.PositiveIntegerField(default=0) #detekcja
    hide_base = models.PositiveIntegerField(default=0) #kamuflaż
    trade_base = models.PositiveIntegerField(default=0) #handel
    
    #atrybuty bazowe
    power_base = models.PositiveIntegerField(default=1) #moc
    resistance_base = models.PositiveIntegerField(default=1) #wytrzymałość
    dexterity_base = models.PositiveIntegerField(default=1) #sprawność
    perception_base = models.PositiveIntegerField(default=1) #percepcja
    intelligence_base = models.PositiveIntegerField(default=1) #inteligencja
    web_base = models.PositiveIntegerField(default=1) #sieć
    artifice_base = models.PositiveIntegerField(default=1) #spryt

    #Addytywne premie do statystyk głównych
    hp_additive = models.PositiveIntegerField(default=10) #punkty życia
    ap_additive = models.PositiveIntegerField(default=100) #punkty akcji
    speed_additive = models.PositiveIntegerField(default=100) #prędkość
    
    #Addytywne premie do umiejętności
    detection_additive = models.PositiveIntegerField(default=0) #detekcja
    hide_additive = models.PositiveIntegerField(default=0) #kamuflaż
    trade_additive = models.PositiveIntegerField(default=0) #handel
    
    #Addytywne premie do atrybutów
    power_additive = models.PositiveIntegerField(default=1) #moc
    resistance_additive = models.PositiveIntegerField(default=1) #wytrzymałość
    dexterity_additive = models.PositiveIntegerField(default=1) #sprawność
    perception_additive = models.PositiveIntegerField(default=1) #percepcja
    intelligence_additive = models.PositiveIntegerField(default=1) #inteligencja
    web_additive = models.PositiveIntegerField(default=1) #sieć
    artifice_additive = models.PositiveIntegerField(default=1) #spryt
    
    #Procentower premie do statystyk głównych
    hp_percent = models.PositiveIntegerField(default=10) #punkty życia
    ap_percent = models.PositiveIntegerField(default=100) #punkty akcji
    speed_percent = models.PositiveIntegerField(default=100) #prędkość
    
    #Procentower premie do umiejętności
    detection_percent = models.PositiveIntegerField(default=0) #detekcja
    hide_percent = models.PositiveIntegerField(default=0) #kamuflaż
    trade_percent = models.PositiveIntegerField(default=0) #handel
        
    #Procentower premie do atrybutów
    power_percent = models.PositiveIntegerField(default=1) #moc
    resistance_percent = models.PositiveIntegerField(default=1) #wytrzymałość
    dexterity_percent = models.PositiveIntegerField(default=1) #sprawność
    perception_percent = models.PositiveIntegerField(default=1) #percepcja
    intelligence_percent = models.PositiveIntegerField(default=1) #inteligencja
    web_percent = models.PositiveIntegerField(default=1) #sieć
    artifice_percent = models.PositiveIntegerField(default=1) #spryt
             
    def can_pick_talent(self, talent):
        """Sprawdzająca, czy bohater może wybrać dany talent"""
        if not self.has_talent(talent):
            if self.has_required_bloodline_talent(talent.blood_line_requirement):
                if self.has_required_talents_talent(talent):
                    if self.has_required_stats_talent(talent):
                        return True
        return False    
            
    def has_talent(self, talent):
        """Sprawdzająca, czy bohater posiada dany talent"""
        return True if self.talents.filter(id=talent.id) else False
 
    def has_required_bloodline(self, blood_line):
        """Sprawdza, czy bohater posiada wymaganą linię krwii (prawdziwe jeśli wprowadzony jest brak lini krwii)"""
        return True if (not blood_line) or self.blood_line == blood_line else False

    def has_required_stats_talent(self, talent):
        """Sprawdza, czy bohater posiada wymagane statystyki, do wzięcia talentu"""
        if not talent.stats_requirements.all():
            return True
        requirements = talent.stats_requirements.all()
        result = True
        for requirement in requirements:
            if not self.has_required_stat_value(requirement.variable, requirement.value):
                break;
        else:
            return True
        return False
    
    def has_required_stat_value(self, variable, value):
        """Sprawdza czy bohater posiada odpowiednią wartość atrybutu"""
        if variable == 1: 
            return self.power_base >= value
        if variable == 2: 
            return self.resistance_base >= value
        if variable == 3: 
            return self.dexterity_base >= value
        if variable == 4: 
            return self.perception_base >= value
        if variable == 5: 
            return self.intelligence_base >= value
        if variable == 6: 
            return self.web_base >= value
        if variable == 7: 
            return self.artifice_base >= value
        if variable == 8: 
            return self.hp_base >= value
        if variable == 9: 
            return self.ap_base >= value
        if variable == 10: 
            return self.speed_base >= value
        if variable == 11: 
            return self.hide >= value
        if variable == 12: 
            return self.detection >= value
        if variable == 13: 
            return self.trade >= value
        if variable == 14:
            return self.lvl
        raise Exception(u"Statystyka nie obsługiwana przez metodę")
    
    def has_required_talents_talent(self, talent):
        """Sprawdza, czy bohater ma wymagane talenty do wybrania danego talentu"""
        required_list = set(talent.talents_required.values_list('id', flat=True))
        hero_talents = set(self.hero.talents.values_list('id', flat=True))
        if required_list.issubset(hero_talents):
            return True
        return False
    
    def give_talent(self, talent):
        pass

    def equip(self, itemInstance):
        pass
    
    def __unicode__(self):
        return self.name
