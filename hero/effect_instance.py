# coding: utf-8
from django.db import models
from .effect import Effect

__author__ = 'episage'

class EffectInstance(models.Model):
    """Reprezentuje podjedyńczą modyfikację statystyki (np. mocy w statystykach głównych).
    Może być przypisany do talentu, zdolności lub przedmiotu"""

    effect=models.ForeignKey(Effect)
    operator = models.IntegerField(default=0)# 0 -> +, 1 -> *
    value = models.DecimalField(default=23.12, decimal_places=10, max_digits=10)

    def calculate(self, base_value):
        if self.operator:
            return base_value * self.value
        else:
            return base_value * self.value