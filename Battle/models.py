__author__ = 'Mati'
from django.db import models
from hero.models import Hero

class Battle_Log(models.Model):
    hero_id_uno = models.ForeignKey(Hero)           #Bohater atakujący
    hero_id_dos = models.ForeignKey(Hero)           #Bohater atakowany
    hero_hp_uno = models.PositiveIntegerField               #Ilosc hp w %
    hero_hp_dos = models.PositiveIntegerField
    hero_ap = models.PositiveIntegerField                   #Punkty Akcji
    hero_used_programs = models.PositiveIntegerField        #Ilosc wylaczonych programow/wirusow
    hero_obtained_programs = models.PositiveIntegerField    #Ilosc programow/wirusow rzuconych na atakujacego
    hero_lvl_uno = models.PositiveIntegerField
    hero_lvl_dos = models.PositiveIntegerField
    distance = models.PositiveIntegerField
    hero_has_field_uno = models.BooleanField        #Czy atakujacy ma rzucone pole
    hero_has_field_dos = models.BooleanField
    type_of_enemy = models.DecimalField             #Typ przeciwnika
    last_loosed_hp = models.PositiveIntegerField            #Ostatnio stracone hp przez atakujacego
    def __unicode__(self):
        return self.name