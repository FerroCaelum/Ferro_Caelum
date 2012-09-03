from django.db import models

class Item(models.Model):
    count = models.PositiveIntegerField()
    hero = models.ForeignKey('hero.Hero')


class Name(models.Model):
    name = models.CharField(max_length=50)
    item = models.ForeignKey(Item)


class Weapon(models.Model):
    speed = models.PositiveIntegerField()
    hit_bonus = models.IntegerField()
    piercing_dmg = models.IntegerField()
    energetic_dmg = models.IntegerField()
    critical = models.IntegerField()
    item = models.ForeignKey(Item)

#armor.
class Armature(models.Model):
    speed_mod = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    camouflage = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class Helmet(models.Model):
    energy_def = models.PositiveIntegerField()
    piercing_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    detector = models.PositiveIntegerField()
    programs_def = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class Program(models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    duration = models.FloatField() # timedelta
    item = models.ForeignKey(Item)


class FieldTech(models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_def = models.PositiveIntegerField()
    strike_def = models.PositiveIntegerField()
    range_def = models.PositiveIntegerField()
    durability = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    item = models.ForeignKey(Item)


class WebTech(models.Model):
    speed = models.PositiveIntegerField()
    pool = models.PositiveIntegerField()
    energy_dmg = models.PositiveIntegerField()
    strike_dmg = models.PositiveIntegerField()
    piercing_dmg = models.PositiveIntegerField()
    critic = models.PositiveIntegerField()
    item = models.ForeignKey(Item)

#oh what the fuck
class SpecialProperties(models.Model):
    item = models.ForeignKey(Item)