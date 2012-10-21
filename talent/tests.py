# coding: utf-8

from django.test import TestCase
from talent.models import Talent
from effect.models import Effect


class TalentsEffectsTest(TestCase):
    def setUp(self):
        self.name1 = "Overpower III"
        self.talent1 = Talent(name=self.name1)
        self.talent1.save()
        self.talent1.effects.create(value=5, variable=4, percent=False, where_works=1)
        
class TalentsTreeTest(TestCase):
    def setUp(self):
        self.name1 = "Overpower III"
        self.name3="Overpower I"
        self.name2 = "Overpower II"
        self.name4="Power III"
        self.name5 = "Power II"
        self.name6 = "Power I"
        self.talent1 = Talent(name=self.name1)
        self.talent1.save()
        self.talent1.talents_required.create(name=self.name2)
        
    def test_one_side_relation(self):
        self.assertFalse(
                self.talent1.talents_required.all() ==
                self.talent1.talents_required.all()[0].talents_required.all())
        
    def test_for_one_talent_requirament(self):
        self.assertEqual(self.talent1.get_talent_requirements_description(),
                          u"Wymagane talenty: " + self.name2)
        
    def test_more_then_one_child(self):
        self.talent1.talents_required.create(name=self.name3)
        self.talent1.talents_required.create(name=self.name4)
        self.assertEqual(
            self.talent1.get_talent_requirements_description(),
            u"Wymagane talenty: " + self.name2 + ", " + self.name3 + ", " + self.name4)

    def test_many_children_parents(self):
        self.talent1.talents_required.create(name=self.name3)
        self.talent1.talents_required.create(name=self.name4)
        self.talent1.talents_required.all()[0].talents_required.create(name=self.name4)
        self.talent1.talents_required.all()[0].talents_required.create(name=self.name5)
        self.assertEqual(
            self.talent1.get_talent_requirements_description(),
            u"Wymagane talenty: " + self.name2 + ", " + self.name3 + ", " + self.name4)
        self.assertEqual(
            self.talent1.talents_required.all()[0].get_talent_requirements_description(),
            u"Wymagane talenty: " + self.name4 + ", " + self.name5)
