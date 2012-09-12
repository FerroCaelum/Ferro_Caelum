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
        AbilityRequierment, created = AbilityRequierment.objects.get_or_create(
            ability_require=self,
            ability_required=person)
        return relationship
    def remove_required_ability(self, ability):
        AbilityRequierment.objects.filter(
             ability_require=self,
             ability_required=ability).delete()
        return     
    def __unicode__(self):
        return self.name
   
class AbilityRequierment(models.Model):
    ability_require = models.ForeignKey(Ability, related_name='require')
    ability_required = models.ForeignKey(Ability, related_name='required')
    
class StatsRequierment(models.Model):
    ability = models.ForeignKey(Ability)
    stats_requirement = models.PositiveIntegerField()
    
class Effect(models.Model): 
    ability = models.ForeignKey(Ability)
    value = models.SmallIntegerField();
    variable_position = models.PositiveSmallIntegerField();
    percent = models.BooleanField();
    active_informations = models.PositiveSmallIntegerField(null=True) #not supported
    def get_variable_string(self, where, dic=None): #not supported
        if dic==None:
            dic = stats_dictionary.dictionary()
        return dic.get_stats_name(self.variable_position, where)
    def get_value_unit(self):
        return '%' if self.percent else ''
    def get_description(self, ability):
        des = self.get_variable_string(ability.where_works) + ' o '                       
        if self.value>=0: des += '+'     
        return des + str(self.value) + self.get_value_unit()  
    def __unicode__(self):
        return ("Efekt "+str(self.id))
