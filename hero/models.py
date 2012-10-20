# coding: utf-8

from django.db import models
import armory.models
from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent

class Owner(models.Model):
    name = models.CharField(max_length=50)

    max_load = models.DecimalField(max_digits=10, decimal_places=2, default=80)
    load = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def give(self, item, new_owner, count):
        """
        Przekazuje item nowemu właścicielowi.

        :param new_owner: komu przekazać item'y
        :type new_owner: hero.Owner
        :param count: ilość
        :type count: int
        :returns: przekazane item'y
        :rtype: Items
        """
        assert item is armory.models.Item
        assert new_owner is Owner
        assert count is int

        if not item.tradeable: raise u'%s is not tradeable.' % self.name
        itemInstances = armory.models.ItemInstance.objects.filter(owner=self, item=item)
        itemInstancesCount = itemInstances.count()
        if itemInstancesCount <= 0: raise u'%s does not have any of %s.' % self.name, item.name
        if itemInstancesCount > 0: raise u'Server error! Item=%s Owner=%s.' % item.name, self.name
        itemInstance = itemInstances[0]
        ownedCount = itemInstance.count
        if ownedCount < count: raise u'%s cannot give more than they have of %s.' % self.name, item.name
        itemInstance.count -= count
        itemInstance.item.spawn(count, new_owner)

    def __unicode__(self):
        return u'%s' % self.name


class Stat(models.Model):
    name = models.CharField(max_length=50)
    value = models.BigIntegerField(default=0)


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