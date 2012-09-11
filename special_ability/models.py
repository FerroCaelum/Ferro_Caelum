# coding: utf-8

from django.db import models
from blood_line.models import BloodLine
import stats_dictionary


class Ability(models.Model):
    name = models.CharField(max_length=50)
    additional_description = models.CharField(max_length=200)
    abilities_requirements = models.ManyToManyField('self', through='AbilityRequierment',
                                                    symmetrical=False, related_name='requires')
    blood_line_requirement = models.ForeignKey(BloodLine, null=True, defult=null)
    activation_informations = models.PositiveSmallIntegerField() #gdzie i w jaki sposób jest aktywowana  
    def howwhere_activated_code(self):
        return self.activation_informations / 10
    def how_activated_code(self):
        return self.activation_informations % 10
    def where_activated(self):
        if self.where_activated_code() == 1:
             return "statystyki glowne"
        if self.where_activated_code() == 2:
             return "statystyki bojowe"
        if self.where_activated_code() == 3:
             return "statystyki niebojowe"
        if self.where_activated_code() == 4:
             return "progres"
        raise ValueError("Druga cyfra activation_informations jest błędna")
    def how_activated(self):
        if self.how_activated_code() == 1:
             return "paszwna"
        if self.how_activated_code() == 2:
             return "aktzwowana"
        raise ValueError("Pierwsza cyfra activation_informations jest błędna")
    def get_descriptions(self, sequence):
         descriptions = self.additional_description + ' '
         for effect in sequence:
             descriptions += effect.get_description(self) + "; "
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
    effect = models.PositiveIntegerField()
    active_informations = models.PositiveSmallIntegerField(blank=True, defult=None) #not supported
    def get_value(self):
        if (self.effect % 10000) / 1000:
            return -1 * self.effect % 1000
        return self.effect % 1000
    def get_variable_name(self, where=self.ability.where_activated_code()): #not supported
        return stats_dictionary.get_stats_name((self.effect % 1000000) / 10000, where)
    def get_value_unit_code(self):
        return (self.effect % 10000000) / 1000000   
    def get_value_unit(self):
        return '%' if self.get_value_unit_code()==2 else ''
    def get_description(self, ability=self.ability):
        description = 'Zmienia ' + self.get_variable_name(ability.where_activated_code()) + ' o '
        if (self.effect % 10000) / 1000 == 0:
            description += '-'
        elif (self.effect % 10000) / 1000 == 1:
            description += '+' 
        else:
             raise ValueError("Czwarta cyfra effect jest błędna")                            
        return descripion + self.get_value()+ self.get_value_unit()                
    def __unicode__(self):
        return ("Efekt %d zdolnosci " % (self.effect))
