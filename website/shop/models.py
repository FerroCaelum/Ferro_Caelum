from django.db import models
from website.hero.models import Item, Owner

__author__ = 'episage'

class Shop(Owner):
    dioaw = models.IntegerField()


class ShopItem(Item):
    price = models.PositiveIntegerField()