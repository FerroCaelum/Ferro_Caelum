# coding: utf-8

from django.db import models

"""
Wszystkie statystyki odnoszące się do bohatera powinne być w 1 tabeli.

Większość wartości defaultowych nie będzie używanych z uwagi na fakt, że statsy każdego bohatera będą przypisywane przy
rejestracji w zależności od wyboru linii krwi, czy innych "rzeczy".

Poprawiłem angielskie nazwy.
"""

class Owner(models.Model):
    max_load = models.DecimalField(max_digits=10, decimal_places=2) #+funkcja agregująca obecny ładunek (nie umiem)
    name = models.CharField(
        max_length=50
    ) # http://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields

    def __unicode__(self):
        return u'%s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, default=0)

    #    def spawn(self, count):
    #        return ItemInstance(item=self, owner=None, count=count)

    def spawn(self, count, owner):
        return ItemInstance(item=self, owner=owner, count=count)

    def __unicode__(self):
        return u'%s' % self.name


class ItemInstance(models.Model):
    item = models.ForeignKey(Item)
    owner = models.ForeignKey(Owner)
    count = models.PositiveIntegerField()

    def give(self, new_owner, count=count):
        if count <= 0:
            self.delete()
            self.save()
            return u'You do not have any %s' % self
        if count > self.count:
            return u'You can not give more than you have.'
        if count == self.count:
            self.owner = new_owner
            return u'%s passed to %s' % (self, new_owner)
        if count < self.count:
            self.count -= count
            new_owner_iis = ItemInstance.objects.filter(owner=new_owner, item=self.item)
            if new_owner_iis.count() == 1:
                new_owner_iis[0].count += count
            elif new_owner_iis > 1:
                raise u"Something very bad happened in db."
            else:
                new_instance = ItemInstance(item=self.item, owner=new_owner, count=count)
                new_instance.save()
            return u'%s passed to %s' % (self, new_owner)

    def __unicode__(self):
        return u'%s[%s]' % (self.item, self.count)


class Being():
    pass


class CanTakeDmg():
    hp = models.PositiveIntegerField(default=10) #punkty życia
    pass


class CanGiveDmg():
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    pass


class Hero(Being, CanTakeDmg, CanGiveDmg, Owner):
    lvl = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=20)

    #atrybuty
    power = models.PositiveIntegerField(default=1) #moc
    resistance = models.PositiveIntegerField(default=1.0) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1.0) #zręczność
    perception = models.PositiveIntegerField(default=1.0) #percepcja
    intelligence = models.PositiveIntegerField(default=1.0) #inteligencja
    web = models.PositiveIntegerField(default=1.0) #sieć
    artifice = models.PositiveIntegerField(default=1.0) #spryt

    #statystyki główne
    #CanTakeDmg
    #CanGiveDmg
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

    #założone
    #   melee_weapon = models.OneToOneField(ItemInstance,related_name="melee")
    #range_weapon = models.OneToOneField(ItemInstance)


    #inne

    max_memory = models.DecimalField(max_digits=10, decimal_places=2) #+to samo

    def Attack(self, hero):
        pass


class BattleContext():
    def __init__(self, beings):
        self.beings = beings
        pass


class Board():
    pass

# sorry ale jak mam to testować w kosoli i robić importy z różnych klas to mnie strzela. dla wygody musze
# to tu przerzucic na chwile


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
    item = models.ForeignKey(Item)