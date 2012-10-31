# coding: utf-8

from django.db import models
import armory.models
from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent

class Stat(models.Model):
    """Bazowa statustyka herosa"""
    hero = models.ForeignKey(Hero)
    """Backreference do Hero"""
    name = models.CharField(max_length=50)
    """Pełna nazwa, którą można wyświetlić użytkownikowi"""
    value = models.BigIntegerField(default=0) # coś jak BLOB bez data type
    """
    Uniwersalna wartość statystyki.
    Przy wyświetlaniu możemy ją dowolnie sformatować w zależności od id/nazwy.
    IMO taki format(bigint) bardzo ułatwi modyfikowanie statystyk.
    """


class Owner(models.Model):
    name = models.CharField(max_length=50)
    """Nazwa np. Rycerz Tomek, Sklepikarz z Aden, Jurand ze Spychowa, etc"""
    max_load = models.ForeignKey(Stat)
    """Max udźwig"""
    load = models.ForeignKey(Stat)
    """Obecny udźwig"""

    def give(self, itemInstance, new_owner, count):
        """
        Przekazuje item nowemu właścicielowi.
        """
        assert itemInstance is armory.models.ItemInstance
        assert new_owner is Owner
        assert count is int

        if not itemInstance.item.tradeable:# czy itemem można handlować?
            raise Exception(u'%s is not tradeable.' % self.name)
        if itemInstance.owner != self: # czy item należy do mnie?
            raise Exception(u'Cannot give not yours item.')

        ownedCount = itemInstance.count
        if ownedCount < count: # czy mam wystarczająco dużo itema?
            raise Exception(u'%s cannot give more than they have of %s.' % self.name,
                itemInstance.item.name)
        itemInstance.count -= count
        itemInstance.item.spawn(count, new_owner)

    #    def can_carry(self, itemInstance):
    #        """
    #        Zwraca true/false w zależności czy Owner może udźwign
    #        """

    def __unicode__(self):
        return u'%s' % self.name


class Hero(Owner):
    lvl = models.PositiveIntegerField(default=1)
    lvl_points = models.PositiveIntegerField(default=100)
    blood_line = models.ForeignKey(BloodLine, null=True)
    profession = models.ForeignKey(Profession, null=True)
    experience = models.PositiveIntegerField(default=0)
    talent = models.ManyToManyField(Talent, null=True)
    #atrybuty
    energy = models.ForeignKey(Stat)
    energy_regeneration = models.ForeignKey(Stat)
    power = models.ForeignKey(Stat) #moc
    resistance = models.ForeignKey(Stat) #wytrzymałość
    dexterity = models.ForeignKey(Stat) #sprawność
    perception = models.ForeignKey(Stat) #percepcja
    intelligence = models.ForeignKey(Stat) #inteligencja
    web = models.ForeignKey(Stat) #sieć
    artifice = models.ForeignKey(Stat) #spryt
    #statystyki główne
    hp = models.ForeignKey(Stat) #punkty życia
    ap = models.ForeignKey(Stat) #punkty akcji
    speed = models.ForeignKey(Stat) #prędkość
    #umiejętności
    detection = models.ForeignKey(Stat) #detekcja
    hide = models.ForeignKey(Stat) #kamuflaż
    trade = models.ForeignKey(Stat) #handel
    melee_attack = models.ForeignKey(Stat) #atak wręcz
    range_attack = models.ForeignKey(Stat) #atak dystansowy
    programming = models.ForeignKey(Stat) #programowanie
    web_use = models.ForeignKey(Stat) #używanie sieci
    antivirus_use = models.ForeignKey(Stat) #obrona antywirusowa
    dodge = models.ForeignKey(Stat) #uniki
    quick_move = models.ForeignKey(Stat) #szybkie poruszanie się
    detection_use = models.ForeignKey(Stat) #wykrywanie
    hide_use = models.ForeignKey(Stat) #ukrywanie się
    trade_use = models.ForeignKey(Stat) #handlowanie

    def equip(self, itemInstance, location):
        """Zakłada item"""
        assert itemInstance is armory.models.ItemInstance
        assert location is armory.models.ItemSlot

        if itemInstance.owner != self:
            raise Exception(u'Cannot equip not ur item.')
        if itemInstance.location is not None:
            raise Exception(u'Item already equipped.')
        if self.lvl < itemInstance.item.min_lvl:
            raise Exception(u'Ur too low lvl to equip this item.')
        itemInstance.location = location
        itemInstance.save()

    def take_off(self, itemInstance):
        """Zdejmuje item"""
        assert itemInstance is armory.models.ItemInstance

        if itemInstance.owner != self:
            raise Exception(u'Cannot take off not ur item.')
        itemInstance.location = None
        itemInstance.save()

    def __unicode__(self):
        return self.name