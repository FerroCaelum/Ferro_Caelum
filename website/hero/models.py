# coding: utf-8

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

"""
Wszystkie statystyki odnoszące się do bohatera powinne być w 1 tabeli.

Większość wartości defaultowych nie będzie używanych z uwagi na fakt, że statsy każdego bohatera będą przypisywane przy
rejestracji w zależności od wyboru linii krwi, czy innych "rzeczy".

Poprawiłem angielskie nazwy.
"""

class Owner(models.Model):
    name = models.CharField(
        max_length=50) # http://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields

    def __unicode__(self):
        return self.name


class Hero(Owner):
    energy = models.PositiveIntegerField(default=0.0)

    #atrybuty
    power = models.PositiveIntegerField(default=1.0) #moc
    resistance = models.PositiveIntegerField(default=1.0) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1.0) #zręczność
    perception = models.PositiveIntegerField(default=1.0) #percepcja
    intelligence = models.PositiveIntegerField(default=1.0) #inteligencja
    web = models.PositiveIntegerField(default=1.0) #sieć
    artifice = models.PositiveIntegerField(default=1.0) #spryt

    #statystyki główne
    hp = models.PositiveIntegerField(default=10) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    speed = models.PositiveIntegerField(default=5) #prędkość http://pl.wikipedia.org/wiki/Kilometr_na_godzin%C4%99

    #statystyki bojowe
    hiding = models.PositiveIntegerField(default=0.0) #ukrywanie
    detection = models.PositiveIntegerField(default=0.0) #detekcja

    #umiejętności walki
    melee_attack = models.PositiveIntegerField(default=0.0) #atak wręcz
    range_attack = models.PositiveIntegerField(default=0.0) #atak dystansowy
    programming = models.PositiveIntegerField(default=0.0) #programowanie
    web_use = models.PositiveIntegerField(default=0.0) #używanie sieci
    antivirus_use = models.PositiveIntegerField(default=0.0) #obrona antywirusowa
    dodge = models.PositiveIntegerField(default=0.0) #uniki
    hiding_use = models.PositiveIntegerField(default=0.0) #ukrywanie się
    detection_use = models.PositiveIntegerField(default=0.0) #wykrywanie
    quick_move = models.PositiveIntegerField(default=1.0) #szybkie poruszanie się

# sorry ale jak mam to testować w kosoli i robić importy z różnych klas to mnie strzela. dla wygody musze
# to tu przerzucic na chwile

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, default=0)

    def spawn(self, count):
        return ItemInstance(item=self, owner=None, count=count)

    def spawn(self, count, owner):
        return ItemInstance(item=self, owner=owner, count=count)

    #    class Meta:
    #        abstract=True

    def __unicode__(self):
        return self.name


class ItemInstance(models.Model):
    item = models.ForeignKey(Item)
    owner = models.ForeignKey(Owner)
    count = models.PositiveIntegerField()

    def give(self, new_owner):
        self.owner = new_owner

    def give(self, new_owner, count):
        if count <= 0:
            self.delete()
            self.save()
            return 'You do not have any ' + str(self)
        if count > self.count:
            return 'You can not give more than you have.'
        if count == self.count:
            self.give(new_owner)
        if count < self.count:
            self.count -= count
            new_owner_items = ItemInstance.objects.filter(owner=new_owner, item=self.item)
            if new_owner_items.count() == 1:
                new_owner_items[0].count += count
            elif new_owner_items > 1:
                raise Exception('Something bad happened in db.')
            else:
                new_instance = ItemInstance(item=self.item, owner=new_owner, count=count)
                new_instance.save()
            return str(count) + ' of ' + str(self) + ' passed to ' + str(new_owner)

    def __unicode__(self):
        return str(self.count) + ' of ' + self.item.name


def FillDb():
    from django.core.management import call_command

    call_command('reset', 'hero')

    rycerz = Hero(name='rycerz tomek')
    rycerz.save()

    miecz = Weapon(
        name='miecz',
        speed=2,
        hit_bonus=4,
        piercing_dmg=12,
        energetic_dmg=0,
        critical=20
    )
    miecz.save()
    miecze = miecz.spawn(2, rycerz)
    miecze.save()

    grosz = Item(
        name='Grosz',
        weight=0.00164
    )
    grosz.save()

    zloty = Item(
        name=u'Złoty',
        weight=0.005
    )
    zloty.save()
    #tak jak jak w realu

    zlote = zloty.spawn(10, rycerz)
    zlote.save()


class Weapon(Item):
    speed = models.PositiveIntegerField()
    hit_bonus = models.IntegerField()
    piercing_dmg = models.IntegerField()
    energetic_dmg = models.IntegerField()
    critical = models.IntegerField()

#    item = models.ForeignKey(Item)


class Armature(Item):
    speed_mod = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    camouflage = models.PositiveIntegerField()

#    item = models.ForeignKey(Item)


class Helmet(Item):
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    detector = models.PositiveIntegerField()
    programs_def = models.PositiveIntegerField()

#    item = models.ForeignKey(Item)


class Program(Item):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    duration = models.FloatField() # timedelta

#    item = models.ForeignKey(Item)


class FieldTech(Item):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    range_def = models.PositiveIntegerField()
    durability = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

#    item = models.ForeignKey(Item)


class WebTech(Item):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_dmg = models.PositiveIntegerField()
    strike_dmg = models.PositiveIntegerField()
    piercing_dmg = models.PositiveIntegerField()
    critic = models.PositiveIntegerField()

#    item = models.ForeignKey(Item)


class SpecialProperties(models.Model):
    item = models.ForeignKey(Item)