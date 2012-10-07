__author__ = 'Mati'
from django.db import models
from hero.models import Hero
class Battle(models.Model):
    hero_uno = models.ForeignKey(Her)
    hero_dos = models.ForeignKey(Her)

    """
    Wszystkie możliwe akcje do wykonania podczas walki, h1 - ten co wykonuje, h2 - na kogo wykonuje
    """

    def close_attack(self,h1,h2):
        return "later"

    def distance_attack(self,h1,h2):
        return "later"

    def get_closer(self,h1,h2):
        return "later"

    def throw_virus(self,h1,h2):
        return "later"

    def throw_programm(self,h1,h2):
        return "later"

    def activate_field(self,h1):
        return "later"

    def web_attack(self,h1,h2):
        return "later"

    def abort(self,h1):
        return "later"
