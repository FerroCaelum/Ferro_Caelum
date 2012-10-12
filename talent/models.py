# coding: utf-8

from django.db import models
from blood_line.models import BloodLine
from effect.models import Effect
import general.stats_dictionary

class Talent(models.Model):
    """Przy awnsie można go wybrać przy awansie, jeśli posiada się wymagane talenty i ma wystarczające wartości statystyk.
    Niektóre talenty są zarezerwowane tylko dla konkretnych linii krwi"""
    name = models.CharField(max_length=50)
    effects = models.ManyToManyField(Effect)
    additional_description = models.CharField(max_length=200, blank=True)
    stats_requirements = models.ManyToManyField(StatsRequirement, blank=True)
    talent_requirements = models.ManyToManyField('self', through='TalentRequierment',
                                                    symmetrical=False, related_name='requires')
    blood_line_requirement = models.ForeignKey(BloodLine, null=True)  
   
    def add_required_talent(self, talent):
        """Dodaje do wymagań talent, który trzeba wziąć by wykupić talent, z którego jest wywołana metoda"""
        talent_requierment, created = TalentRequierment.objects.get_or_create(
            require=self,
            required=talent)
        return talent_requierment
    
    def remove_required_talent(self, talent):
        """Usuwa wymagany talent, konieczny do wykupienia talentu, z którego jest wywołana ta metoda"""
        TalentRequierment.objects.filter(
             require=self,
             required=talent).delete()
        return     
    
    def get_talents_requierments(self):
        """Zwraca listę talentów, wymaganych do wykupienia talentu, z którgo jest wywoływana ta metoda"""
        return self.talent_requirements.filter(
             required__require=self)
        
    def get_effects(self):
        """Zwraca listę efektów przypisanych do"""
        pass
    
    def get_stats_requierments(self):
        """Zwraca listę wymagań w statystykach, potrzebnych do wykupienia talentu, z którego jest woływana ta metoda"""
        return StatsRequierment.objects.filter(talent__pk=self.pk)
    
    def get_talent_requirements_description(self):
        """Zwraca słowny opis wymaganych talentów, potrzebnych do wykupienia talentu, z którgo jest wywoływana ta metoda"""
        requiraments = self.get_talent_requirements()
        descriptions = self.name + ' wymaga: '
        for a in requiraments:
            descriptions +=  a.__unicode__()
            if a!=requiraments[requiraments.count()-1]:  descriptions += ", "  
        return descriptions      
     
    def get_stats_requirements_description(self):
         """Zwraca słowny opis wymaganych statystyk, potrzebnych do wykupienia talentu, z którgo jest wywoływana ta metoda"""
         requiraments = self.get_stats_requierments()
         descriptions = self.name + ' wymaga '
         for r in requiraments:
             descriptions +=  r.get_description(self)
             if r!=requiraments[requiraments.count()-1]:  descriptions += ", "
         return descriptions

    def get_effects_description(self):
         """Zwaca słowny opis efektów zapewnianych przez talent"""
         effects = self.get_effects()
         descriptions = self.name + ' zmienia: '
         for e in effects:
             descriptions +=  e.get_description()
             if e!=effects[effects.count()-1]:  descriptions += ", "
         return descriptions
     
    def __unicode__(self):
        return self.name
   
   
class TalentRequierment(models.Model):
    """Klasa potrzebna do budowy drzewa rozwoju talentów"""
    require = models.ForeignKey(Talent, related_name='require')
    required = models.ForeignKey(Talent, related_name='required')
    
class StatsRequirement(models.Model):
    """Wymagania w statystykach bohatera"""
    talent = models.ForeignKey(Talent)
    value = models.PositiveSmallIntegerField();
    variable = models.PositiveSmallIntegerField();
    def get_variable_string(self, where):
        return stats_dictionary.get_stats_name(self.variable, where)
    def get_description(self, talent):
        des = self.get_variable_string(1) + ': '                           
        return des + str(self.value)       
    def __unicode__(self):
        return "Wymaganie statystyk " + str(self.id)
