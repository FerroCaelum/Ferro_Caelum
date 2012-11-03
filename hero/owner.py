# coding: utf-8
from django.db import models
from hero.items.item_instance import ItemInstance
from hero.statistic import Statistic

class Owner(models.Model):
    # Nazwa np. Rycerz Tomek, Sklepikarz z Aden, Jurand ze Spychowa, etc
    name = models.CharField(max_length=50)

    # Level
    lvl = models.PositiveIntegerField(default=1)

    # Max udźwig
    max_load = models.PositiveIntegerField(default=1)

    # Obecny udźwig
    load =  models.PositiveIntegerField(default=1)

    def equip(self, itemInstance, location):
        """Zakłada item"""
        assert itemInstance is ItemInstance
        assert location is str

        if itemInstance.owner != self:
            raise Exception(u'Cannot equip not ur item.')
        itemInstance.location = ItemInstance.LOCATION_FLAGS[location]

    def take_off(self, itemInstance):
        """Zdejmuje item"""
        assert itemInstance is ItemInstance

        if itemInstance.owner != self:
            raise Exception(u'Cannot take off not ur item.')
        itemInstance.location = None

    def give(self, itemInstance, new_owner, count):
        """Przekazuje item nowemu właścicielowi."""
        assert itemInstance is ItemInstance
        assert new_owner is Owner
        assert count is int

        if not itemInstance.item.tradeable:# czy itemem można handlować?
            raise Exception(u'%s is not tradeable.' % self.name)
        if itemInstance.owner != self: # czy item należy do mnie?
            raise Exception(u'Cannot give not yours item.')

        if itemInstance.count < count: # czy mam wystarczająco dużo itema?
            raise Exception(u'%s cannot give more than they have of %s.' % self.name,
                itemInstance.item.name)
        itemInstance.count -= count # zabieramy item sobie
        itemInstance.item.spawn(count, new_owner) # spawnujemy u nowego właściciela

    def item(self, location):
        """
        Zwraca item, który znajduje się w location.
        Wywołanie: owner.item("LeftHand")
        """
        items = ItemInstance.objects.filter(owner=self)
        location_flag = ItemInstance.LOCATION_FLAGS[location]
        for item in items:
            if item.location & location_flag == location_flag:
                return item
        return None

    def __unicode__(self):
        return u'%s' % self.name