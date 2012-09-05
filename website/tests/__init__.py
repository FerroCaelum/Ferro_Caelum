# coding: utf-8
__author__ = 'episage'

from website.hero.models import *
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
