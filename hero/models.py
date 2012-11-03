# coding: utf-8
from django.db import models
import armory.models
from blood_line.models import BloodLine
from effect.models import EffectInstance
from profession.models import Profession

class Stat(models.Model):
    base = models.BigIntegerField(default=10)
    value = models.BigIntegerField(default=10)
    effects = models.ManyToManyField(EffectInstance)

class Owner(models.Model):
    # Nazwa np. Rycerz Tomek, Sklepikarz z Aden, Jurand ze Spychowa, etc
    name = models.CharField(max_length=50)

    # Level
    lvl = models.PositiveIntegerField(default=1)

    # Max udźwig
    max_load =  models.ForeignKey(Stat, related_name="max_load")

    # Obecny udźwig
    load =  models.ForeignKey(Stat, related_name="load")

    def give(self, itemInstance, new_owner, count):
        """Przekazuje item nowemu właścicielowi."""
        assert itemInstance is armory.models.ItemInstance
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
        items = armory.models.ItemInstance.objects.filter(owner=self)
        location_flag = armory.models.ItemInstance.LOCATION_FLAGS[location]
        for item in items:
            if item.location & location_flag == location_flag:
                return item
        return None

    def __unicode__(self):
        return u'%s' % self.name


class Hero(Owner):
    lvl_points = models.PositiveIntegerField(default=0)
    blood_line = models.ForeignKey(BloodLine, null=True)
    profession = models.ForeignKey(Profession, null=True)
    experience = models.PositiveIntegerField(default=0)

    energy = models.ForeignKey(Stat, related_name="energy")
    max_energy = models.ForeignKey(Stat, related_name="max_energy")
    hp = models.ForeignKey(Stat, related_name="hp") # punkty życia
    max_hp=models.ForeignKey(Stat, related_name="max_hp") # max punkty życia
    ap = models.ForeignKey(Stat, related_name="ap") # punkty akcji
    max_ap = models.ForeignKey(Stat, related_name="max_ap") # max punkty akcji
    #atrybuty
#    energy_regeneration = models.ForeignKey(Stat)
#    power = models.ForeignKey(Stat) #moc
#    resistance = models.ForeignKey(Stat) #wytrzymałość
#    dexterity = models.ForeignKey(Stat) #sprawność
#    perception = models.ForeignKey(Stat) #percepcja
#    intelligence = models.ForeignKey(Stat) #inteligencja
#    web = models.ForeignKey(Stat) #sieć
#    artifice = models.ForeignKey(Stat) #spryt

    def equip(self, itemInstance, location):
        """Zakłada item"""
        assert itemInstance is armory.models.ItemInstance
        assert location is str

        if itemInstance.owner != self:
            raise Exception(u'Cannot equip not ur item.')
        itemInstance.location = armory.models.ItemInstance.LOCATION_FLAGS[location]

    def take_off(self, itemInstance):
        """Zdejmuje item"""
        assert itemInstance is armory.models.ItemInstance

        if itemInstance.owner != self:
            raise Exception(u'Cannot take off not ur item.')
        itemInstance.location = None

    def meets_bloodline_requirament(self, talent):
        requirement = talent.blood_line_requirement
        return True if (not requirement) or self.blood_line == requirement else False

    def __unicode__(self):
        return self.name