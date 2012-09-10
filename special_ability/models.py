# coding: utf-8

from django.db import models
from blood_line.models import BloodLine
import stats_dictionary


class Ability(models.Model):
    name = models.CharField(max_length=50)
    additional_description = models.CharField(max_length=200)
    abilities_requirements = models.ManyToManyField('self', through='AbilityRequierment', 
                                                    symmetrical=False, related_name='requires')
    blood_line_requirement = models.ForeignKey(BloodLine, null=True, defult=None)
    activation_informations = models.PositiveSmallIntegerField() #gdzie i w jaki sposób jest aktywowana  
    def howwhere_activated_code(self):
        return self.activation_informations/10
    def how_activated_code(self):
        return self.activation_informations%10
    def where_activated(self):
        if self.where_activated_code()==1:
             return "statystyki glowne"
        if self.where_activated_code()==2:
             return "statystyki bojowe"
        if self.where_activated_code()==3:
             return "statystyki niebojowe"
        if self.where_activated_code()==4:
             return "progres"
        raise ValueError("Druga cyfra activation_informations jest błędna")
    def how_activated(self):
        if self.how_activated_code()==1:
             return "natychmiastowo" # Przy dodaniu specialnej zdolności do statystyk
        if self.how_activated_code()==2:
             return "pasywna"  # Przy każdym przeliczaniu trzeba brać ją pod uwagę
        if self.how_activated_code()==3:
             return "aktywowana" #gracz musi aktywować zdolność; zdolności aktywowane nie będą zakodowane w tej wersj FerroCaelum;
                                 #pozostałe motody ich nie obsługują
        raise ValueError("Pierwsza cyfra activation_informations jest błędna")
#    def sum_effect_descriptions(self, sequence):
#         descriptions=''
#         for effect in sequence:
#             descriptions += self.effect_description(effect) + " "
#         return descriptions
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
#    active_informations = models.PositiveSmallIntegerField() #not supported
    def get_value(self):
        if (self.effect%10000)/1000:
            return -1*self.effect%1000
        return self.effect%1000
    def get_variable_name(self, where=self.ability.where_activated()): #not supported
            return stats_dictionary.get_stats_name((self.effect%1000000)/10000, where)
    def get_description(self, where=self.ability.where_activated()): #not supported
        description = ''
        return description
    def __unicode__(self):
        return ("Efekt %d zdolnosci " % (self.effect))