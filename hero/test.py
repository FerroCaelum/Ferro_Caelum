# coding: utf-8
from armory.models import Item, ItemInstance, ItemPlace
from hero.models import Hero, Owner

import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        self.h1 = Hero(name=u'Książę Karol')
        self.h2 = Hero(name=u'Królowa Karolina')
        self.h1.save()
        self.h2.save()

        reka = ItemPlace(name=u'prawa ręka')
        reka.save()

        cos = Item.objects.all()
        self.sword = Item(u'Srebrny Miecz', reka)
        self.sword.save()
        self.sword.spawn(1, self.h1).save()

    def test_ownership(self):
        foundItems = ItemInstance.objects.filter(owner=self.h1)
        print type(foundItems)
        self.assertEqual(foundItems.count(), 1)
        self.assertEqual(foundItems[0].item.name, u'Srebrny Miecz')

if __name__ == '__main__':
    unittest.main()
