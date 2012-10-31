# coding: utf-8
from armory.models import Item, ItemInstance, ItemSlot
from hero.models import Hero

import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        Hero.objects.all().delete()
        self.h1 = Hero(name=u'Książę Karol')
        self.h2 = Hero(name=u'Królowa Karolina')
        self.h1.save()
        self.h2.save()

        reka = ItemSlot(name=u'prawa ręka')
        reka.save()

        self.sword = Item(name=u'Srebrny Miecz', location=reka, min_lvl=0)
        Item.objects.all().delete()
        self.sword.save()
        self.sword.spawn(1, self.h1).save()

    def test_ownership(self):
        foundItems = ItemInstance.objects.filter(owner=self.h1)
        print type(foundItems)
        self.assertEqual(foundItems.count(), 1)
        self.assertEqual(foundItems[0].item.name, u'Srebrny Miecz')

if __name__ == '__main__':
    unittest.main()
