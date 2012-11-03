# coding: utf-8
from django.db import models
from hero.effect_instance import EffectInstance
from hero.items.item import Item
from hero.owner import Owner

__author__ = 'episage'

class ItemInstance(models.Model):
    """
    Faktyczny, użyteczny w grze item.
    Wszystkie settery są do użytku wewnętrzbego albo do użytku administratora (GMa).
    To dlatego, że nie sprawdzają uprawnień (np. czy jeden gracz może przekazać item drugiemu).
    Te uprawnienia są sprawdzane wyżej - w Hero.
    """

    item = models.ForeignKey(Item)
    _owner = models.ForeignKey(Owner)
    _location = models.PositiveIntegerField(null=True, blank=True, default=None) # flagi z LOCATION_FLAGS
    _count = models.IntegerField(default=1)
    effects = models.ManyToManyField(EffectInstance)

    # Miejsca gdzie można założyć przedmiot.
    # Przedmiot może zajmować więcej niż jedno miejsce.
    # Jeżeli _location jest null to znaczy, że przedmiot nie jest założony.
    # W przeciwnym wypadku jest założony i na bohatera działają efekty z przedmoitu a slot jest zajęty.
    LOCATION_NAMES = {
        # TODO slot który może mieć wiele itemów
        1: "Head",
        2: "LeftHand",
        4: "Torso",
        8: "RightHand",
        16: "Legs",
        32: "Shoes",
        }
    # Odwrotne mapowanie.
    LOCATION_FLAGS = dict((v, k) for k, v in LOCATION_NAMES.iteritems())

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        assert new_owner is Owner

        itemsLoad = self.item.load * self.count
        if new_owner.load + itemsLoad > new_owner.max_load:
            raise Exception(u'Cannot pass xx to xx. Owner cannot bare it.')

        self._owner = new_owner
        self.owner.load -= itemsLoad
        new_owner.load += itemsLoad

        self.save()
        new_owner.save()

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        if self.location is not None:
            raise Exception(u'Item already worn.')
        if self.owner.item(new_location) is not None:
            raise Exception(u'Slot is busy.')
        if (self.item.location & new_location) != self.item.location:
            raise Exception(u'Item does not fit in the slot.')
        if self.owner.lvl > self.item.min_lvl:
            raise Exception(u'You\'re too low lvl.')
        self._location = new_location
        self.save()

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0: raise Exception(u'Negative count? Really?')
        itemLoad = self.item.load
        newLoad = self.owner.load + (itemLoad * self.count - itemLoad * value)
        if newLoad > self.owner.max_load:
            raise Exception(u'Cannot carry additional %s of %s.' % (value - self.count, self.item.name))
        if newLoad < 0:
            raise Exception(u'Load < 0')

        if value == 0:# usuwamy z gry
            self.delete()
        else:
            self._count = value
        self.owner.load = newLoad
        self.save()
        self.owner.save()

    def destroy(self):
        self.delete()

    def __unicode__(self):
        return u'%s[%s]' % (self.item, self.count)