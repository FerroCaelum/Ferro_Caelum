# coding: utf-8
from django.db import models

class Effect(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=800)

    def description(self):
        """Generuje opis działania efektu (z podstawionymi zmiennymi)"""
        #        des = self.get_variable_string() + ' o '
        #        if self.value>=0: des += '+'
        #        return des + str(self.value) + self.get_value_unit()
        pass

    def __unicode__(self):
        return u'Effect %s' % self.name


class EffectInstance(models.Model):
    """Reprezentuje podjedyńczą modyfikację statystyki (np. mocy w statystykach głównych).
    Może być przypisany do talentu, zdolności lub przedmiotu"""

    effect = models.ForeignKey(Effect)
    modifier = models.DecimalField(default=2)

    # True -> mnożenie, False -> dodawanie
    operation = models.BooleanField(default=False)

    def calculate(self, base_value):
        if self.operation:
            return base_value * self.modifier
        else:
            return base_value * self.modifier