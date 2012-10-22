# coding: utf-8

from django.test import TestCase
from effect.models import Effect

class SimpleEffectTest(TestCase):
    def setUp(self):
        self.effect = Effect(value=5, variable=4, percent=False, where_works=1)

    def test_save(self):
        self.effect.save()
        self.assertEqual(Effect.objects.all().get(id=1), self.effect)
        
    def test_get_variable_string(self):
        self.assertEqual(u"percepcja o +5", self.effect.get_description())
