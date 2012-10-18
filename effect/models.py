# coding: utf-8
from django.db import models
import general.stats_dictionary

class Effect(models.Model): 
    """Reprezentuje podjedyńczą modyfikację statystyki (np. mocy w statystykach głównych).
    Może być przypisany do talentu, zdolności lub przedmiotu"""
    STATS_KINDS = (
                  (1, u"Statystyki główne"),
                  (2, u"Statystyki bojowe"),
                  (3, u"Statystkyi niebojowe"),
                  (4, u"Progres"),
                  ) 
    value = models.SmallIntegerField();
    variable = models.PositiveSmallIntegerField();
    percent = models.BooleanField();
    where_works = models.PositiveSmallIntegerField(choices = STATS_KINDS)
    
    def get_variable_string(self):
        """Zwraca nazwę zmiennej, na którą wpływa efekt"""
        return general.stats_dictionary.get_stats_name(self.variable, self.where_works)
    
    def get_value_unit(self):
        """Zwraca jednostkę w jakiej jest podana wartość efektu"""
        return '%' if self.percent else ''
    
    def get_description(self):
        """Generuje opis działania efektu"""
        des = self.get_variable_string() + ' o '                       
        if self.value>=0: des += '+'     
        return des + str(self.value) + self.get_value_unit()  
    
    def __unicode__(self):
        return "Efekt "+str(self.id)