# coding: utf-8

from django.test import TestCase
from blood_line.models import BloodLine
from profession.models import Profession
from hero.models import Hero
from talent.models import *

class HeroTalent(TestCase):
    def setUp(self):
        self.malkavian = BloodLine(name="Malkavian", power=8, resistance=8, dexterity=8,
           perception=9, intelligence=10, web=10, artifice=1, hp=10, ap=100, speed=100, 
           detection=0, hide=2, trade=0)
        self.malkavian.save()
        
        self.knight = Profession(name="knight", power_cost=30, resistance_cost=30,
           dexterity_cost=30, perception_cost=30, intelligence_cost=30, web_cost=30,
           artifice_cost=30, detection_cost=10, hide_cost=10, trade_cost=10)
        self.knight.save()
        
        self.hero = Hero(max_load=100, name="Baron Duck", lvl=200, lvl_points=0,
           blood_line=self.malkavian, profession=self.knight, experience=0, energy=100,
           energy_regeneration=30, gold=12345, power_base=70, resistance_base=170,
           dexterity_base=270, perception_base=370, intelligence_base=470, web_base=570,
           artifice_base=670, hp_base=770, ap_base=870, speed_base=970, detection_base=1070, 
           hide_base=1170, trade_base=1270)
        self.hero.save() 
        
        self.talent1 = Talent(name="Overpower")
        self.talent1.save()
    
    
    def test_has_talent(self):
        #Sprawdza, czy Ma talent!
        self.talent2 = Talent(name="Overpower2")
        self.talent2.save()
        self.hero.talents.add(self.talent1)
        
        self.assertTrue(self.hero.has_talent(self.talent1), "Bohater posiada talent (1 talent)")
        self.assertFalse(self.hero.has_talent(self.talent2), "Bohater nie posiada talentu")
        
        self.hero.talents.add(self.talent2)
        self.assertTrue(self.hero.has_talent(self.talent2), "Bohater posiada talent")
        
    def test_has_required_bloodline(self):
        self.malkavian2 = BloodLine(name="Malkavian2", power=8, resistance=8, dexterity=8, 
           perception=9, intelligence=10, web=10, artifice=1, hp=10, ap=100, speed=100, 
           detection=0, hide=2, trade=0)
        self.malkavian2.save()

        self.talent2 = Talent(name="Overpower2", blood_line_requirement=self.malkavian)
        self.talent2.save()
        self.talent3 = Talent(name="Overpower3", blood_line_requirement=self.malkavian2)
        self.talent3.save()
        
        self.assertTrue(self.hero.has_required_bloodline(self.talent1.blood_line_requirement),
           "Dla talentu z brakiem wymagania lini krwii")
        self.assertTrue(self.hero.has_required_bloodline(self.talent2.blood_line_requirement),
           "Dla talentu z wymaganiem posiadanej lini krwii")
        self.assertFalse(self.hero.has_required_bloodline(self.talent3.blood_line_requirement),
           "Dla talentu z wymaganiem nieposiadanej lini krwii")

    def test_has_required_talents(self):

        self.talent2 = Talent(name="Overpower2")
        self.talent2.save()
        self.talent2.talents_required.add(self.talent1)
        self.assertFalse(self.hero.has_required_talents_talent(self.talent2),
            "Wymagania niespelnione (0 posiadanych talentow)")
        
        self.hero.talents.add(self.talent1)
        self.assertTrue(self.hero.has_required_talents_talent(self.talent2),
            "Wymagania spelnione (1 posiadany talent)")
        
        self.talent3 = Talent(name="Overpower3")
        self.talent3.save()
        self.hero.talents.add(self.talent2)
        self.assertTrue(self.hero.has_required_talents_talent(self.talent3),
            "Wymagania spelnione")
        
        self.talent1.talents_required.add(self.talent3)
        self.assertFalse(self.hero.has_required_talents_talent(self.talent1),
            "Wymagania niespelnione")
        
    def test_has_required_stats_talent(self):
        self.assertTrue(self.hero.has_required_stats_talent(self.talent1),
            "Posiada. Brak wymagan.")
        
        self.stats_requirement1 = StatsRequirement(value=1, variable=1)
        self.stats_requirement1.save()
        self.talent1.stats_requirements.add(self.stats_requirement1)
        self.assertTrue(self.hero.has_required_stats_talent(self.talent1),
            "Posiada. Jedno wymaganie, poniżej wartosci")
        
        self.stats_requirement1.value = 70
        self.stats_requirement1.save()
        self.assertTrue(self.hero.has_required_stats_talent(self.talent1),
            "Posiada. Jedno wymaganie, rownie wartosci")
        
        self.stats_requirement1.value = 71
        self.stats_requirement1.save()
        self.assertFalse(self.hero.has_required_stats_talent(self.talent1),
            "Nie posiada. Jedno wymaganie, powyzej wartosci")
        
        self.stats_requirement2 = StatsRequirement(value=1, variable=1)
        self.stats_requirement2.save()
        self.talent1.stats_requirements.add(self.stats_requirement2)
        self.assertFalse(self.hero.has_required_stats_talent(self.talent1),
            "Nie posiada. Dwa wymaganie, jedno powyżej")
        
        self.stats_requirement1.value = 1
        self.stats_requirement1.save()
        self.stats_requirement2.value = 1
        self.stats_requirement2.save()
        self.assertTrue(self.hero.has_required_stats_talent(self.talent1),
            "Posiada. Dwa wymaganie, poniżej wartosci")