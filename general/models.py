from django.db import models
import stats_dictionary

class Effect(models.Model): 
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
        
        
class Ability(models.Model):
    name = models.CharField(max_length=50)
    additional_description = models.CharField(max_length=200, blank=True)
    passive = models.BooleanField();
    activation_info = models.OneToOneField(ActivationInfo, null=True)
    def get_effects(self):
        return EffectOfAbility.objects.filter(ability__pk=self.pk)
    def get_effects_description(self):
         effects = self.get_effects()
         descriptions = self.name + ' zmienia: '
         for e in effects:
             descriptions +=  e.get_description()
             if e!=effects[effects.count()-1]:  descriptions += ", "
         return descriptions
    def passive_string(self):
        if self.passive:
             return "pasywna"
        return "aktywowana"
    def __unicode__(self):
        return self.name
    
        class Meta:
            abstract = True    
    
class ActivationInfo(models.Model):
    time = models.PositiveSmallIntegerField()