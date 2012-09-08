# coding: utf-8

from django.db import models
from hero.models import Hero
from blood_line.models import BloodLine


class Ability(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    abilities_requirements = models.ManyToManyField('self', through='Ability_requierment', 
                                                    symmetrical=False, related_name='requires')
    blood_line_requirement = models.ForeignKey(BloodLine, blank=True)
    type = models.SmallIntegerField()
    def add_required_ability(self, ability):
        Ability_requierment, created = Ability_requierment.objects.get_or_create(
            ability_require=self,
            ability_required=person)
        return relationship
    def remove_required_ability(self, ability):
        Ability_requierment.objects.filter(
             ability_require=self,
             ability_required=ability).delete()
        return
   
class Ability_requierment(models.Model):
    ability_require = models.ForeignKey(Ability, related_name='require')
    ability_required = models.ForeignKey(Ability, related_name='required')
    
class Stats_requierment(models.Model):
    ability = models.ForeignKey(Ability)
    stats_requirement = models.PositiveIntegerField()
    
class Effect(models.Model): 
    ability = models.ForeignKey(Ability)
    effect = models.PositiveIntegerField()
    hero = models.ManyToManyField(Hero)