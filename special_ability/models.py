# coding: utf-8

from django.db import models
from blood_line.models import BloodLine
from general.models import Effect
import general.stats_dictionary


class SpecialAbility(models.Model):
    abilities_requirements = models.ManyToManyField('self', through='AbilityRequierment',
                                                    symmetrical=False, related_name='requires')
    blood_line_requirement = models.ForeignKey(BloodLine, null=True)
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
    def get_abilities_requierments(self):
        return self.abilities_requirements.filter(
             required__require=self)
    def get_effects(self):
        return EffectOfSpecialAbility.objects.filter(ability__pk=self.pk)
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
         descriptions = self.name + ' wymaga '
         for r in requiraments:
             descriptions +=  r.get_description(self)
             if r!=requiraments[requiraments.count()-1]:  descriptions += ", "
         return descriptions
   
class AbilityRequierment(models.Model):
    require = models.ForeignKey(Ability, related_name='require')
    required = models.ForeignKey(SpecialAbility, related_name='required')
    
class StatsRequirement(models.Model):
    ability = models.ForeignKey(SpecialAbility)
    value = models.PositiveSmallIntegerField();
    variable = models.PositiveSmallIntegerField();
    def get_variable_string(self, where):
        return stats_dictionary.get_stats_name(self.variable, where)
    def get_description(self, ability):
        des = self.get_variable_string(1) + ': '                           
        return des + str(self.value)       
    def __unicode__(self):
        return "Wymaganie statystyk " + str(self.id)
        
    
class EffectOfSpecialAbility(Effect): 
    ability = models.ForeignKey(SpecialAbility)
