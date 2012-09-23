# coding: utf-8
from django.db import models
from hero.models import Owner

__author__ = 'episage'

class BaseItem(models.Model):
    """
    Abstrakcyjna klasa, podstawa do tworzenia itemów.

    Nie wolno tworzyć instancji tej klasy.
    """

    name = models.CharField(max_length=50, unique=True)

    weight = models.DecimalField(max_digits=16, decimal_places=5, default=0)

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
        Tworzy nowy item.
        """
        return Items(item=self, owner=owner, count=count)

    def __unicode__(self):
        return u'%s' % self.name


class Items(models.Model):
    """
    Faktyczny, użyteczny w grze item.
    """

    base_item = models.ForeignKey(BaseItem)

    owner = models.ForeignKey(Owner)

    count = models.PositiveIntegerField()

    def give(self, new_owner, count=count):
        """
        Przekazuje item nowemu właścicielowi.

        :param new_owner: komu przekazać item'y
        :type new_owner: hero.Owner
        :param count: ilość
        :type count: int
        :returns: przekazane item'y
        :rtype: Items
        """
        if count > self.count:
            raise u'You can not give more than you have.'
        if count == self.count:
            self.owner = new_owner
            return self
        if count < self.count:
            new_owner_items = Items.objects.filter(owner=new_owner, base_item=self.base_item)[:1]
            self.count -= count
            self.save()
            if new_owner_items.count() == 1:
                old_items = new_owner_items[0]
                old_items.count += count
                old_items.save()
                return old_items
            else:
                new_items = Items(item=self.base_item, owner=new_owner, count=count)
                new_items.save()
                return new_items

        raise u"Error occured."

    def __unicode__(self):
        return u'%s[%s]' % (self.base_item, self.count)


class Money(BaseItem):
    pass


class Weapon(BaseItem):
    speed = models.PositiveIntegerField()
    hit_bonus = models.IntegerField()
    piercing_dmg = models.IntegerField()
    energetic_dmg = models.IntegerField()
    critical = models.IntegerField()


class Armature(BaseItem):
    speed_mod = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    camouflage = models.PositiveIntegerField()


class Helmet(BaseItem):
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    detector = models.PositiveIntegerField()
    programs_def = models.PositiveIntegerField()


class Program(BaseItem):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    duration = models.FloatField() # timedelta


class FieldTech(BaseItem):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    range_def = models.PositiveIntegerField()
    durability = models.PositiveIntegerField()
    count = models.PositiveIntegerField()


class WebTech(BaseItem):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_dmg = models.PositiveIntegerField()
    strike_dmg = models.PositiveIntegerField()
    piercing_dmg = models.PositiveIntegerField()
    critic = models.PositiveIntegerField()


class SpecialProperties(models.Model):
    item = models.ForeignKey(BaseItem)