# coding: utf-8
from django.db import models
from hero.models import Owner

class Item:
    name = models.CharField(max_length=50, unique=True)
    load = models.DecimalField(max_digits=16, decimal_places=5, default=0)

    #    icon =models.ImageField()
    #
    #    stackable=models.BooleanField(default=True)
    #
    #    sellable=models.BooleanField(default=True)
    #
    #    droppable=models.BooleanField(default=True)
    #
    #    destroyable=models.BooleanField(default=True)
    #
    #    tradeable=models.BooleanField(default=True)
    #
    #    depositable=models.BooleanField(default=True)

    def spawn(self, count, owner):
        """
        Tworzy nowy item z powietrza.
        """
        if count <= 0: raise "Cannot spawn less then 1 items."

        return ItemInstance(item=self, owner=owner, count=count)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.name


class ItemInstance(models.Model):
    """
    Faktyczny, użyteczny w grze item.
    """

    item = models.ForeignKey(Item)
    owner = models.ForeignKey(Owner)
    location = models.ForeignKey(ItemPlace) # plecak, prawa ręka, lewa ręka, buty, etc.
    _count = models.PositiveIntegerField()

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0: raise "Negative count? Really?"
        itemLoad = self.item.load
        newLoad = self.owner.load +\
                  (itemLoad * self.count # current load
                   -
                   itemLoad * value) # new load
        if newLoad > self.owner.max_load:
            raise u'Itanz be to heavy'
        if newLoad < 0:
            raise u'OMG! HALP! Load<0!'

        if value == 0:
            self.delete()
        else:
            self._count = value
        self.owner.load = newLoad

    def __unicode__(self):
        return u'%s[%s]' % (self.base_item, self.count)


class ItemPlace(models.Model):
    name = models.CharField()


class Money(Item, models.Model):
    pass


class Weapon(Item, models.Model):
    speed = models.PositiveIntegerField()
    hit_bonus = models.IntegerField()
    piercing_dmg = models.IntegerField()
    energetic_dmg = models.IntegerField()
    critical = models.IntegerField()


class Armature(Item, models.Model):
    speed_mod = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    camouflage = models.PositiveIntegerField()


class Helmet(Item, models.Model):
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    detector = models.PositiveIntegerField()
    programs_def = models.PositiveIntegerField()


class Program(Item, models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    duration = models.FloatField() # timedelta


class FieldTech(Item, models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    range_def = models.PositiveIntegerField()
    durability = models.PositiveIntegerField()
    count = models.PositiveIntegerField()


class WebTech(Item, models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_dmg = models.PositiveIntegerField()
    strike_dmg = models.PositiveIntegerField()
    piercing_dmg = models.PositiveIntegerField()
    critic = models.PositiveIntegerField()


class SpecialProperties(models.Model):
    item = models.ForeignKey(ItemInstance)