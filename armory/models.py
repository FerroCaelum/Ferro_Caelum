# coding: utf-8
from django.db import models
from hero.models import Owner

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    load = models.DecimalField(max_digits=16, decimal_places=5, default=0)
    min_lvl = models.PositiveIntegerField(default=0)

    #icon = models.ImageField()
    sellable = models.BooleanField(default=True)
    destroyable = models.BooleanField(default=True)
    tradeable = models.BooleanField(default=True)
    enchantable = models.BooleanField(default=True)

    def effects(self):
        """Returns effects item produces"""
        pass

    def spawn(self, count, owner):
        """
        Tworzy nowy item z powietrza, a jak już jest w ekwipunku to zwiększa jego ilość.
        """
        if count <= 0:
            raise Exception(u'Cannot spawn less then 1 items.')

        items = ItemInstance.objects.filter(owner=owner, item=self)
        itemsCount = items.count()
        if itemsCount > 1:
            raise Exception(u'Player has 2 same item instances. Something very bad happened.')
        if itemsCount == 1:
            items[0].count += count
            return items[0]
        if itemsCount == 0:
            newItem = ItemInstance(item=self, count=count, owner=owner)
            newItem.save()
            return newItem

    def __unicode__(self):
        return u'%s' % self.name


class ItemInstance(models.Model):
    """
    Faktyczny, użyteczny w grze item.
    Wszystkie settery są do użytku wewnętrzbego albo do użytku administratora (GMa).
    To dlatego, że nie sprawdzają uprawnień (np. czy jeden gracz może przekazać item drugiemu).
    Te uprawnienia są sprawdzane wyżej - w Hero.
    """
    LOCATION_FLAGS = {
        # 0: "Somewhere", #slot który może mieć wiele itemów TODO
        1: "Head",
        2: "LeftHand",
        4: "Torso",
        8: "RightHand",
        16: "Legs",
        32: "Shoes",
    }
    """Miejsca gdzie można założyć przedmiot.
    Przedmiot może zajmować więcej niż jedno miejsce.
    Jeżeli _location jest null to znaczy, że przedmiot nie jest założony.
    W przeciwnym wypadku jest założony i na bohatera działają efekty z przedmoitu a slot jest zajęty."""

    item = models.ForeignKey(Item)
    _owner = models.ForeignKey(Owner)
    _location = models.PositiveIntegerField(null=True, blank=True,
        default=None)# null = plecak reszta może być:
    # prawa ręka, lewa ręka, buty, etc. zgodnie z LOCATION_FLAGS
    _count = models.IntegerField(default=1)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        assert new_owner is Owner

        itemsLoad = self.item.load * self.count
        if new_owner.load + itemsLoad > new_owner.max_load:
            raise Exception(u'Cannot pass xx to xx. Iteems too heavy.')

        self._owner = new_owner
        self.owner.load -= itemsLoad
        new_owner.load += itemsLoad

        self.save()
        new_owner.save()

    @property
    def location(self):
        return self._owner

    @location.setter
    def location(self, new_location):
        if self.location is not None:
            raise Exception(u'Item already worn.')
        """toDO LOGIKA statsow"""
        self._location = new_location

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0: raise Exception(u'Negative count? Really?')
        itemLoad = self.item.load
        newLoad = self.owner.load + (itemLoad * self.count -
                                     itemLoad * value)
        if newLoad > self.owner.max_load:
            raise Exception(u'Cannot carry additional x of xxx.')
        if newLoad < 0:
            raise Exception(u'Load < 0')

        if value == 0:# usuwamy z gry
            self.delete()
        else:
            self._count = value
        self.owner.load = newLoad

    def destroy(self):
        self.delete()

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