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
    
    talents = models.ManyToManyField(Talent)
    
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
    #>Umiejętności[MinValueValidator(0.0)], default=0.0
    detection_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #ukrywanie się
    trade_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #handlowanie 
    
    def get_statistic(self, number):
        """Metoda zwracająca wartość statystyki o podanym numerze. UWAGA: metoda niekompletna"""
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
        if number == 14:
            return self.lvl
        raise u"Statystyka nie obsługiwana przez metodę"
        
    def get_updated_statistic(self, number):
        """Metoda zwracająca wartość statystyki o danym numerze z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących. UWAGA: metoda niekompletna - uwzględnia efekty pochodzące jedynie od talentów"""
        if number > 10: raise u'Statystyka nieobsługiwana.'
        tes = set() #Zbiór wszystkich efektów addytywnych wpływajacych na daną statystykę,
                      # pobrana ze wszystkich talentów bohatera
        tem = set() #Zbiór wszystkich efektów multiplikatywnych wpływajacych na daną statystykę,
                      # pobrana ze wszystkich talentów bohatera
        s = 0
        m = 100
        talents = self.talents.all()
            
        for t in talents:
            tes.add(t.effects.filter(where_works = number).filter(variable = number).filter(percent = False))
        for t in talents:
            tes.add(t.effects.filter(where_works = number).filter(variable = number).filter(percent = True))
            
        for effects_set in tes:
            for e in effects_set:
                s += e.value   
            
        for effects_set in tem:
            for e in effects_set:
                m += e.value   
                
        stat = self.get_statistic(number)       
        if stat:
			up_stats = 0.01*m*(stat+s)
			if up_stats<1:
				return 1
			else:
				return up_stats
        else: 
            return stat
    
    def get_updated_power(self):
        """Metoda zwracająca wartość mocy bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(1)
    
    def get_updated_resistance(self):
        """Metoda zwracająca wartość wytrzymałości bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(2)
    def get_updated_dexterity(self):
        """Metoda zwracająca wartość sprawności bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(3)
    
    def get_updated_perception(self):
        """Metoda zwracająca wartość percepcji bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(4)
    
    def get_updated_intelligence(self):
        """Metoda zwracająca wartość inteligencji bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(5)
    
    def get_updated_web(self):
        """Metoda zwracająca wartość sieci bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(6)
    
    def get_updated_artifice(self):
        """Metoda zwracająca wartość zaradności bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(7)
    
    def get_updated_hp(self):
        """Metoda zwracająca ilość punktów życia bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(8)
    
    def get_updated_ap(self):
        """Metoda zwracająca wartość punktów akcji bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(9)
    
    def get_updated_speed(self):
        """Metoda zwracająca wartość szybkości bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(10)
    
    def have_talent(self, talent):
        """Metoda sprawdzająca, czy bohater posiada dany talent"""
        return True if self.talents.filter(pk__contains=talent.pk) else False
    
    def have_required_stat(self, number, value):
        if number == 1: 
            return self.power >= value
        if number == 2: 
            return self.resistance >= value
        if number == 3: 
            return self.dexterity >= value
        if number == 4: 
            return self.perception >= value
        if number == 5: 
            return self.intelligence >= value
        if number == 6: 
            return self.web >= value
        if number == 7: 
            return self.artifice >= value
        if number == 8: 
            return self.hp >= value
        if number == 9: 
            return self.ap >= value
        if number == 10: 
            return self.speed >= value
        if number == 14:
            return self.lvl
        raise u"Statystyka nie obsługiwana przez metodę"
    
    def meets_stats_requirements(self, talent):
        pass
    
    def meets_talents_requiraments(self, talent):
        pass
    
    def meets_bloodline_requirament(self,talent):
        requirement = talent.blood_line_requirement
        return True if (not requirement) or self.blood_line == requirement else False
            
    def can_pick_talent(self, talent):
        """Metoda sprawdzająca, czy bohater może wybrać dany talent"""
        if self.meets_bloodline_requirament(talent):
            if self.meets_talents_requiraments(talent):
                if self.meets_stats_requirements(talent):
                    return True
        return False    
	
    def __unicode__(self):
        return self.name