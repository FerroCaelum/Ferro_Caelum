# coding: utf-8
__author__ = 'episage'

from django.db import models
from hero.hero import *

class Shop(Owner):
    pass


class ShopItem(models.Model):
    def get_price(self, hero):
        raise NotImplementedError()