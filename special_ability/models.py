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
    def get_description(self):
         effects = Effect.objects.filter(ability__pk=self.pk)
         descriptions = self.name + ' zmienia: '
         for e in effects:
             descriptions +=  e.get_description(self)
             if e!=effects[effects.count()-1]:  descriptions += ", "
         return descriptions
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
    def __unicode__(self):
        return self.name
   
class AbilityRequierment(models.Model):
    require = models.ForeignKey(Ability, related_name='require')
    required = models.ForeignKey(Ability, related_name='required')
    
class StatsRequierment(models.Model):
    ability = models.ForeignKey(Ability)
    stats_requirement = models.PositiveIntegerField()
    
class Effect(models.Model): 
    ability = models.ForeignKey(Ability)
    value = models.SmallIntegerField();
    variable_position = models.PositiveSmallIntegerField();
    percent = models.BooleanField();
    active_informations = models.PositiveSmallIntegerField(null=True) #not supported
    def get_variable_string(self, where): #not supported
        return stats_dictionary.get_stats_name(self.variable_position, where)
    def get_value_unit(self):
        return '%' if self.percent else ''
    def get_description(self, ability):
        des = self.get_variable_string(ability.where_works) + ' o '                       
        if self.value>=0: des += '+'     
        return des + str(self.value) + self.get_value_unit()  
    def __unicode__(self):
        return ("Efekt "+str(self.id))
