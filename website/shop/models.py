# coding: utf-8
__author__ = 'episage'

from django.db import models
from hero.models import Item, Owner, ItemInstance

class Shop(Owner):
    pass


class ShopItem(models.Model):
    def get_price(self, hero):
        raise NotImplementedError()