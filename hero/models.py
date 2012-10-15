# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator
import armory.models
from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent

class Owner(models.Model):
    name = models.CharField(max_length=50)

    max_load = models.DecimalField(max_digits=10, decimal_places=2, default=80)
    load = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def give(self, item, new_owner, count):
        """
        Przekazuje item nowemu właścicielowi.

        :param new_owner: komu przekazać item'y
        :type new_owner: hero.Owner
        :param count: ilość
        :type count: int
        :returns: przekazane item'y
        :rtype: Items
        """

        assert item is armory.models.Item
        assert new_owner is Owner
        assert count is int

        if not item.tradeable: raise u'%s is not tradeable.' % self.name
        itemInstances = armory.models.ItemInstance.objects.filter(owner=self, item=item)
        itemInstancesCount = itemInstances.count()
        if itemInstancesCount <= 0: raise u'%s does not have any of %s.' % self.name, item.name
        if itemInstancesCount > 0: raise u'Server error! Item=%s Owner=%s.' % item.name, self.name
        itemInstance = itemInstances[0]
        ownedCount = itemInstance.count
        if ownedCount < count: raise u'%s cannot give more than they have of %s.' % self.name, item.name
        itemInstance.count -= count
        itemInstance.item.spawn(count, new_owner)

    def __unicode__(self):
        return u'%s' % self.name


class Hero(Owner):
    lvl = models.PositiveIntegerField(default=1)
    lvl_points = models.PositiveIntegerField(default=100)
    blood_line = models.ForeignKey(BloodLine, null=True)
    profession = models.ForeignKey(Profession, null=True)
    experience = models.PositiveIntegerField(default=0)
    energy = models.PositiveIntegerField(default=20)
    energy_regeneration = models.PositiveIntegerField(default=20)
    gold = models.DecimalField(max_digits=20, decimal_places=2, default=0.0) #stan konta
    talent = models.ManyToManyField(Talent, null=True)
    #atrybuty
    power = models.PositiveIntegerField(default=1) #moc
    resistance = models.PositiveIntegerField(default=1) #wytrzymałość
    dexterity = models.PositiveIntegerField(default=1) #sprawność
    perception = models.PositiveIntegerField(default=1) #percepcja
    intelligence = models.PositiveIntegerField(default=1) #inteligencja
    web = models.PositiveIntegerField(default=1) #sieć
    artifice = models.PositiveIntegerField(default=1) #spryt
    #statystyki główne
    hp = models.PositiveIntegerField(default=10) #punkty życia
    ap = models.PositiveIntegerField(default=100) #punkty akcji
    speed = models.PositiveIntegerField(default=100) #prędkość
    #umiejętności
    detection = models.PositiveIntegerField(default=0) #detekcja
    hide = models.PositiveIntegerField(default=0) #kamuflaż
    trade = models.PositiveIntegerField(default=0) #handel
    #wyćwiczenie (doświadczenie)
    #>Bojowe
    melee_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #atak wręcz
    range_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #atak dystansowy
    programming = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #programowanie
    web_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #używanie sieci
    antivirus_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #obrona antywirusowa
    dodge = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #uniki
    quick_move = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #szybkie poruszanie się
    #>Umiejętności
    detection_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #ukrywanie się
    trade_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)],
        default=0.0) #handlowanie

    def equip(self, itemInstance):
        pass


    def __unicode__(self):
        return self.name