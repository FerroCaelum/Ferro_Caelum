# coding: utf-8

from django.test import TestCase
from talent.models import Talent
from effect.models import Effect


class TalentsEffectsTest(TestCase):
    def setUp(self):
        self.talent1 = Talent(name="Overpower III")
        self.talent1.save()
        self.talent1.effects.create(value=5, variable=4, percent=False, where_works=1)
    
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)
        
class TalentsTreeTest(TestCase):
    def setUp(self):
        self.talent1 = Talent(name="Overpower III")
        self.talent1.save()
        self.talent1.talents_required.create(name="Overpower II")
        
    def test_if_one_side_relation(self):
        self.assertFalse(
                self.talent1.talents_required.all() ==
                self.talent1.talents_required.all()[0].talents_required.all())
