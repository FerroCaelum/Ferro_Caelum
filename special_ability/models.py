# coding: utf-8

from django.db import models
from blood_line.models import BloodLine
import stats_dictionary


class Ability(models.Model):
    name = models.CharField(max_length=50)
    additional_description = models.CharField(max_length=200, blank=True)
    abilities_requirements = models.ManyToManyField('self', through='AbilityRequierment',
                                                    symmetrical=False, related_name='requires')
    blood_line_requirement = models.ForeignKey(BloodLine, null=True)
    where_works = models.PositiveSmallIntegerField()
    passive = models.BooleanField();
    def add_required_ability(self, ability):
        ability_requierment, created = AbilityRequierment.objects.get_or_create(
            require=self,
            required=ability)
        return ability_requierment
    def remove_required_ability(self, ability):
        AbilityRequierment.objects.filter(
             require=self,
             required=ability).delete()
        return     
    def get_abilities_requirements(self):
        return self.abilities_requirements.filter(
             required__require=self)
    def get_effects(self):
        return Effect.objects.filter(ability__pk=self.pk)
    def get_stats_requierments(self):
        return StatsRequierment.objects.filter(ability__pk=self.pk)
    def get_abilities_requirements_description(self):
         requiraments = self.get_abilities_requirements()
         descriptions = self.name + ' wymaga: '
         for a in requiraments:
             descriptions +=  a.__unicode__()
             if a!=requiraments[requiraments.count()-1]:  descriptions += ", "  
         return descriptions      
    def get_stats_requirements_description(self):
         requiraments = self.get_stats_requierments()
         descriptions = self.name + ' wymaga: '
         for r in requiraments:
             descriptions +=  r.get_description(self)
             if r!=requiraments[requiraments.count()-1]:  descriptions += ", "
         return descriptions
    def get_effects_description(self):
         effects = self.get_effects()
         descriptions = self.name + ' zmienia: '
         for e in effects:
             descriptions +=  e.get_description(self)
             if e!=effects[effects.count()-1]:  descriptions += ", "
         return descriptions
    def where_works_string(self):
        if self.where_works == 1:
             return "statystyki glowne"
        if self.where_works == 2:
             return "statystyki bojowe"
        if self.where_works == 3:
             return "statystyki niebojowe"
        if self.where_works == 4:
             return "progres"
    def passive_string(self):
        if self.passive:
             return "pasywna"
        return "aktzwowana"
    def __unicode__(self):
        return self.name
   
class AbilityRequierment(models.Model):
    require = models.ForeignKey(Ability, related_name='require')
    required = models.ForeignKey(Ability, related_name='required')
    
class StatsRequierment(models.Model):
    ability = models.ForeignKey(Ability)
    value = models.PositiveSmallIntegerField();
    variable = models.PositiveSmallIntegerField();
    def get_variable_string(self, where):
        return stats_dictionary.get_stats_name(self.variable, where)
    def get_description(self, ability):
        des = self.get_variable_string(ability.where_works) + ': '                           
        return des + str(self.value)       
    def __unicode__(self):
        return "Wymaganie statystyk" + str(self.id)
        
    
class Effect(models.Model): 
    ability = models.ForeignKey(Ability)
    value = models.SmallIntegerField();
    variable = models.PositiveSmallIntegerField();
    percent = models.BooleanField();
    active_informations = models.PositiveSmallIntegerField(null=True) #not supported
    def get_variable_string(self, where):
        return stats_dictionary.get_stats_name(self.variable, where)
    def get_value_unit(self):
        return '%' if self.percent else ''
    def get_description(self, ability):
        des = self.get_variable_string(ability.where_works) + ' o '                       
        if self.value>=0: des += '+'     
        return des + str(self.value) + self.get_value_unit()  
    def __unicode__(self):
        return "Efekt "+str(self.id)
