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
import sys


class HeroEffectsTest(TestCase):
    def setUp(self):
        self.malkavian = BloodLine(name="Malkavian", power=8, resistance=8, dexterity=8, perception=9, intelligence=10, web=10, artifice=1,
                              hp=10, ap=100, speed=100, detection=0, hide=2, trade=0)
        self.malkavian.save()
        self.knight = Profession(name="knight", power_cost=30, resistance_cost=30, dexterity_cost=30, perception_cost=30, intelligence_cost=30,
                                 web_cost=30, artifice_cost=30, detection_cost=10, hide_cost=10, trade_cost=10)
        self.knight.save()
        self.hero=Hero(max_load=100, name="Baron Duck", lvl=200, lvl_points=0, blood_line=self.malkavian, profession=self.knight, 
                       experience=0,
                       energy=100, energy_regeneration=30, gold=12345, power=90, resistance=290, dexterity=390, perception=490, intelligence=590, 
                       web=690, artifice=790, hp=300, ap=200, speed=350, detection=890, hide=990, trade=1090)
        self.hero.save() 


        
    def test_update_power(self):
        self.talent1 = Talent(name="Overpower")
        self.talent1.save()
        self.effect1 = EffectOfTalent(talent = self.talent1, value = 10, variable = 1, percent = False, where_works = 1)
        self.effect2 = EffectOfTalent(talent = self.talent1, value = 30, variable = 1, percent = True, where_works = 1)
        self.effect3 = EffectOfTalent(talent = self.talent1, value = 20, variable = 2, percent = True, where_works = 1)
        self.effect4 = EffectOfTalent(talent = self.talent1, value = 30, variable = 1, percent = False, where_works = 2)
        self.effect1.save()
        self.effect2.save()
        self.effect3.save()
        self.effect4.save()
        self.hero.talent.add(self.talent1)
        self.assertEqual(self.hero.get_updated_power(), 130)
