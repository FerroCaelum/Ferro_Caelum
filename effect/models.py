# coding: utf-8
from django.db import models
from talent.models import Talent
from ability.models import Ability
import general.stats_dictionary

class Effect(models.Model): 
    """Reprezentuje podjedyńczą modyfikację statystyki (np. mocy w statystykach głównych).
    Może być przypisany do talentu, zdolności lub przedmiotu"""
    value = models.SmallIntegerField();
    variable = models.PositiveSmallIntegerField();
    percent = models.BooleanField();
    where_works = models.PositiveSmallIntegerField()
    def where_works_string(self):
        if self.where_works == 1:
             return "statystyki glowne"
        if self.where_works == 2:
             return "statystyki bojowe"
        if self.where_works == 3:
             return "statystyki niebojowe"
        if self.where_works == 4:
             return "progres"
    def get_variable_string(self):
        return stats_dictionary.get_stats_name(self.variable, self.where_works)
    def get_value_unit(self):
        return '%' if self.percent else ''
    def get_description(self):
        des = self.get_variable_string() + ' o '                       
        if self.value>=0: des += '+'     
        return des + str(self.value) + self.get_value_unit()  
    def __unicode__(self):
        return "Efekt "+str(self.id)
    
        class Meta:
            abstract = True
            
class EffectOfTalent(Effect): 
    talent = models.ForeignKey(Talent)
    
class EffectOfAbility(Effect):
    ability = models.ForeignKey(Ability)