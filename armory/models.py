# coding: utf-8
from django.db import models
from hero.models import Owner

class ItemPlace(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
#    def __init__(self, name, location, load=1, min_lvl=0):
#        models.Model.__init__(self)
#        self.name=name
#        self.location=location
#        self.load=load
#        self.min_lvl=min_lvl
    name = models.CharField(max_length=50, unique=True)
    load = models.DecimalField(max_digits=16, decimal_places=5, default=0)
    location = models.ForeignKey(ItemPlace, null=True, blank=True,
        default=None) # plecak, prawa ręka, lewa ręka, buty, etc.
    min_lvl = models.PositiveIntegerField()

    #icon = models.ImageField()
    sellable = models.BooleanField(default=True)
    destroyable = models.BooleanField(default=True)
    tradeable = models.BooleanField(default=True)
    enchantable = models.BooleanField(default=True)

    def spawn(self, count, owner):
        """
        Tworzy nowy item z powietrza.
        """
        if count <= 0: raise Exception(u'Cannot spawn less then 1 items.')

        return ItemInstance(item=self, count=count, owner=owner)

    def __unicode__(self):
        return u'%s' % self.name


class ItemInstance(models.Model):
    """
    Faktyczny, użyteczny w grze item.
    """

    def __init__(self, item, count, owner):
        models.Model.__init__(self)
        self.owner = owner
        self.item = item
        self._count = count

    item = models.ForeignKey(Item)
    owner = models.ForeignKey(Owner)
    equipped = models.BooleanField(default=False)
    _count = models.IntegerField()

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0: raise Exception(u'Negative count? Really?')
        itemLoad = self.item.load
        newLoad = self.owner.load + (itemLoad *
                                     self.count -
                                     itemLoad *
                                     value)
        if newLoad > self.owner.max_load:
            raise Exception(u'Item is too heavy.')
        if newLoad < 0:
            raise Exception(u'Load < 0')

        if value == 0:
            self.delete()
        else:
            self._count = value
        self.owner.load = newLoad

    def destroy(self):
        self.delete()

    def equip(self):
        if self.item.location == None: raise Exception(u'Item not equipable')
        self.equipped = True


    def give(self):
        pass

    def __unicode__(self):
        return u'%s[%s]' % (self.item, self.count)


class Money(Item):
    pass


class Weapon(Item):
    speed = models.PositiveIntegerField()
    hit_bonus = models.IntegerField()
    piercing_dmg = models.IntegerField()
    energetic_dmg = models.IntegerField()
    critical = models.IntegerField()


class Armature(Item):
    speed_mod = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    camouflage = models.PositiveIntegerField()


class Helmet(Item):
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    detector = models.PositiveIntegerField()
    programs_def = models.PositiveIntegerField()


class Program(Item):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    duration = models.FloatField() # timedelta


class FieldTech(Item):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    range_def = models.PositiveIntegerField()
    durability = models.PositiveIntegerField()
    count = models.PositiveIntegerField()


class WebTech(Item):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_dmg = models.PositiveIntegerField()
    strike_dmg = models.PositiveIntegerField()
    piercing_dmg = models.PositiveIntegerField()
    critic = models.PositiveIntegerField()


class SpecialProperties(models.Model):
    item = models.ForeignKey(ItemInstance)