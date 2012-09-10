# coding: utf-8

from django.db import models
from blood_line.models import BloodLine


class Ability(models.Model):
    name = models.CharField(max_length=50)
    additional_description = models.CharField(max_length=200)
#    abilities_requirements = models.ManyToManyField('self', through='AbilityRequierment', 
#                                                    symmetrical=False, related_name='requires')
#    blood_line_requirement = models.ForeignKey(BloodLine, null=True, defult=None)
    when_and_where = models.SmallIntegerField()
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
    
    def effect_description(self, e):
        description={
                     }
        return description
    
    def sum_effect_descriptions(self, sequence):
         descriptions=''
         for effect in sequence:
             descriptions += self.effect_description(effect) + " "
         return descriptions
    def ability_type(self):
        if (self.when_and_where/100)%10==3:
            return "aktywna"
        else:
            return "pasywna"
    def get_description(self):
        return self.additional_description +" "+self.sum_effect_descriptions(Effect.objects.filter(ability__pk=self.pk))
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
    def description(self, a=ability):
        return
    def __unicode__(self):
        return ("Efekt %d zdolnosci " % (self.effect))