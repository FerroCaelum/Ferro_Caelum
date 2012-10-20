"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

from django.test import TestCase
from blood_line.models import BloodLine
from profession.models import Profession
from hero.models import Hero
from talent.models import *
from effect.models import *

class HeroTalents(TestCase):
    def setUp(self):
        self.malkavian = BloodLine(name="Malkavian", power=8, resistance=8, dexterity=8, perception=9, intelligence=10, web=10, artifice=1,
                              hp=10, ap=100, speed=100, detection=0, hide=2, trade=0)
        self.malkavian.save()
        self.knight = Profession(name="knight", power_cost=30, resistance_cost=30, dexterity_cost=30, perception_cost=30, intelligence_cost=30,
                                 web_cost=30, artifice_cost=30, detection_cost=10, hide_cost=10, trade_cost=10)
        self.knight.save()
        self.hero=Hero(max_load=100, name="Baron Duck", lvl=200, lvl_points=0, blood_line=self.malkavian, profession=self.knight, 
                       experience=0,
                       energy=100, energy_regeneration=30, gold=12345, power=70, resistance=170, dexterity=270, perception=370, intelligence=470, 
                       web=570, artifice=670, hp=770, ap=870, speed=970, detection=1070, hide=1170, trade=1270)
        self.hero.save() 
    
    
    def test_contains(self):
        self.talent1 = Talent(name = "Overpower")
        self.talent1.save()
        self.talent2 = Talent(name = "Overpower2")
        self.talent2.save()
        self.hero.talents.add(self.talent1)
        
        self.assertTrue(self.hero.have_talent(self.talent1), "Bohater posiada talent")
        self.assertFalse(self.hero.have_talent(self.talent2), "Bohater nie posiada talentu")
        
        
    def test_meets_bloodline_requirament(self):
        self.malkavian2 = BloodLine(name="Malkavian2", power=8, resistance=8, dexterity=8, perception=9, intelligence=10, web=10, artifice=1,
                              hp=10, ap=100, speed=100, detection=0, hide=2, trade=0)
        self.malkavian2.save()
        
        self.talent1 = Talent(name = "Overpower")
        self.talent1.save()
        self.talent2 = Talent(name = "Overpower2", blood_line_requirement = self.malkavian)
        self.talent2.save()
        self.talent3 = Talent(name = "Overpower3", blood_line_requirement = self.malkavian2)
        self.talent3.save()
        
        self.assertTrue(self.hero.meets_bloodline_requirament(self.talent1), "Dla talentu z brakiem wymagania lini krwii")
        self.assertTrue(self.hero.meets_bloodline_requirament(self.talent2), "Dla talentu z wymaganiem posiadanej lini krwii")
        self.assertFalse(self.hero.meets_bloodline_requirament(self.talent3), "Dla talentu z wymaganiem nieposiadanej lini krwii")



class HeroUpdateStatistics(TestCase):
    def setUp(self):
        self.malkavian = BloodLine(name="Malkavian", power=8, resistance=8, dexterity=8, perception=9, intelligence=10, web=10, artifice=1,
                              hp=10, ap=100, speed=100, detection=0, hide=2, trade=0)
        self.malkavian.save()
        self.knight = Profession(name="knight", power_cost=30, resistance_cost=30, dexterity_cost=30, perception_cost=30, intelligence_cost=30,
                                 web_cost=30, artifice_cost=30, detection_cost=10, hide_cost=10, trade_cost=10)
        self.knight.save()
        self.hero=Hero(max_load=100, name="Baron Duck", lvl=200, lvl_points=0, blood_line=self.malkavian, profession=self.knight, 
                       experience=0,
                       energy=100, energy_regeneration=30, gold=12345, power=70, resistance=170, dexterity=270, perception=370, intelligence=470, 
                       web=570, artifice=670, hp=770, ap=870, speed=970, detection=1070, hide=1170, trade=1270)
        self.hero.save() 
        
        
    def test_one_effect(self):
        self.hero.talents.create(name = "Overpower")
        self.hero.talents.all()[0].effects.create(value = 10, variable = 1, percent = False, where_works = 1)
        self.assertEqual(self.hero.power+10, self.hero.get_updated_statistic(1))
        
        
    def test_many_effect(self):
        self.hero.talents.create(name = "Overpower")
        talent = self.hero.talents.all()[0]
        talent.effects.create(value = 10, variable = 1, percent = False, where_works = 1)
        talent.effects.create(value = 20, variable = 1, percent = False, where_works = 1)
        talent.effects.create(value = 15, variable = 1, percent = True, where_works = 1)
        talent.effects.create(value = 25, variable = 1, percent = True, where_works = 1)
        talent.effects.create(value = 1000, variable = 2, percent = False, where_works = 1)
        talent.effects.create(value = 1000, variable = 1, percent = False, where_works = 2)
        self.assertEqual((self.hero.power + 30) * 1.4, self.hero.get_updated_statistic(1))
        
        
    def test_many_talents(self):
        talents_set = set()
        add_number = 10
        for i in range(1, add_number+1):
            talent = Talent(name = "talent "+str(i))
            talent.save()
            talent.effects.create(value = 1, variable = 1, percent = False, where_works = 1)
            self.hero.talents.add(talent)
        self.assertEqual(self.hero.power + add_number, self.hero.get_updated_statistic(1))
            
            
    def test_many_talents_many_effects(self):
        talents_set = set()
        add_number = 10
        for i in range(1, add_number+1):
            talent = Talent(name = "talent "+str(i))
            talent.save()
            talent.effects.create(value = 1, variable = 1, percent = False, where_works = 1)
            talent.effects.create(value = 2, variable = 1, percent = False, where_works = 1)
            talent.effects.create(value = 3, variable = 1, percent = True, where_works = 1)
            talent.effects.create(value = 4, variable = 1, percent = True, where_works = 1)
            self.hero.talents.add(talent)
        self.assertEqual((self.hero.power + 3*add_number)*1.7, self.hero.get_updated_statistic(1))
		
        
	def test_min_border(self):
		self.hero.talents.all()[0].effects.create(value = -self.hero.power, variable = 1, percent = False, where_works = 1)
		self.assertEqual(1, self.hero.get_updated_statistic(1))
        
    
        


