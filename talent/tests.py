# coding: utf-8

from django.test import TestCase
from talent.models import Talent
from effect.models import Effect


class SimpleTest(TestCase):
    def setUp(self):
        self.talent1 = Talent(name="Overpower III")
    
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
