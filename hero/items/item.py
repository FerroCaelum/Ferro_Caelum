# coding: utf-8
from django.db import models


__author__ = 'episage'

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    load = models.PositiveIntegerField(default=0)
    min_lvl = models.PositiveIntegerField(default=0)
    location = models.PositiveIntegerField(default=0) # LOCATION_FLAGS

    # icon = models.ImageField()
    sellable = models.BooleanField(default=True)
    destroyable = models.BooleanField(default=True)
    tradeable = models.BooleanField(default=True)
    enchantable = models.BooleanField(default=True)

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
            items[0].save()
            return items[0]
        if itemsCount == 0:
            newItem = ItemInstance(item=self, count=count, owner=owner)
            newItem.save()
            return newItem

    def __unicode__(self):
        return u'%s' % self.name