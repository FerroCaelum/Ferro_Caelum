# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator

from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent

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

    STATS = {
                1: "power",
                2: "resistance",
                3: "dexterity",
                4: "perception",
                5: "intelligence",
                6: "web",
                7: "artifice",
                8: "hp",
                9: "ap",
                10: "speed",
                11: "detection",
                12: "hide",
                13: "trade"
                }

    STATS_BASE = {
                1: "power_base",
                2: "resistance_base",
                3: "dexterity_base",
                4: "perception_base",
                5: "intelligence_base",
                6: "web_base",
                7: "artifice_base",
                8: "hp_base",
                9: "ap_base",
                10: "speed_base",
                11: "detection_base",
                12: "hide_base",
                13: "trade_base"
                }
    
    STATS_ADDITIVE = {
                1: "power_additive",
                2: "resistance_additive",
                3: "dexterity_additive",
                4: "perception_additive",
                5: "intelligence_additive",
                6: "web_additive",
                7: "artifice_additive",
                8: "hp_additive",
                9: "ap_additive",
                10: "speed_additive",
                11: "detection_additive",
                12: "hide_additive",
                13: "trade_additive"
                }
        
    STATS_PERCENT = {
                1: "power_percent",
                2: "resistance_percent",
                3: "dexterity_percent",
                4: "perception_percent",
                5: "intelligence_percent",
                6: "web_percent",
                7: "artifice_percent",
                8: "hp_percent",
                9: "ap_percent",
                10: "speed_percent",
                11: "detection_percent",
                12: "hide_percent",
                13: "trade_percent"
                }
    
    
    def statistic_base(self, number):
        return getattr(self, self.STATS_BASE[number])
    
    def statistic_additive(self, number, add=None):
        value = getattr(self, self.STATS_ADDITIVE[number])
        if add != 0:
            setattr(self, self.STATS_ADDITIVE[number], value + add)
            return value + add
        return value
    
    def statistic_percent(self, number, add=0):
        value = getattr(self, self.STATS_PERCENT[number])
        if add != 0:
            setattr(self, self.STATS_PERCENT[number], value + add)
            return value + add
        return value
    
    def statistic(self, number, new_value=None):
        if set != None:
            setattr(self, self.STATS[number], new_value)
            return new_value
        return getattr(self, self.STATS[number])
     
     
    def give_talent(self, talent):
        """Sprawdza, czy bohater spełnia wmagania talentu i jeśli tak to dodaje mu go. Zwraca True jeśli operacja jest udana i false jeśli bohater nie spełnia wymagań."""
        if self.can_pick_talent(talent):
            self.add_talent(talent)
            return True
        return False      
            
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
        return self.statistic_base(variable) >= value
    
    def has_required_talents_talent(self, talent):
        """Sprawdza, czy bohater ma wymagane talenty do wybrania danego talentu"""
        required_list = set(talent.talents_required.values_list('id', flat=True))
        hero_talents = set(self.hero.talents.values_list('id', flat=True))
        if required_list.issubset(hero_talents):
            return True
        return False
    
    
    def add_talent(self, talent):
        """Dodaje bohaterowi i nanosi poprawki z efektów talentu na jego statystyki. UWAGA: przed zastosowaniem metody powinno się sprawdzić, czy bohater spełnia wymagania"""
        self.talents.add(talent)
        for number in range(1, 13):
            add = 0
            effects_additive = talent.effects.filter(where_works=number).filter(variable=number).filter(percent=False)
            for e in effects_additive:
                add += e.value
            self.statistic_additive(number, add)
            
            percent = 0
            effects_percent = talent.effects.filter(where_works=number).filter(variable=number).filter(percent=True)
            for e in effects_percent:
                percent += e.value
            self.statistic_percent(number, percent)
 
            self.update_stats(number)
        self.save()

    def update_stats(self, number):
        current_value = self.statistic(number)
        additive = self.statistic_additive(number)
        if additive + current_value < 1:
            additive = 1 - current_value
        
        percent = self.statistic_percent(number)   
        new_value = 0.01 * (100 + percent) * (current_value + additive)
        
        if new_value > 0:
            self.statistic(number, new_value)
        else:
            self.statistic(number, 1)
            

    def equip(self, itemInstance):
        pass
    
    
    def __unicode__(self):
        return self.name

import armory.models


