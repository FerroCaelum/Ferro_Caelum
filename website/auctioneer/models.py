# coding: utf-8
from armory.models import BaseItem

__author__ = 'episage'

from django.db import models
from hero.models import *
import datetime

class AuctionHouse(Owner):
    def put_up(self, ii, min_price, valid_from, valid_to):
        if not valid_from < valid_to < datetime.datetime.now(): raise u"err"
        if min_price < 0: return u"Minimal price must be greater or equal to zero."
        if not ii.owner == self:
            ii.owner = self

        ai = AuctionItem(
            item=ii,
            min_price=min_price,
            valid_from=valid_from,
            valid_to=valid_to
        )
        ai.save()
        return ai


class AuctionItem(models.Model):
    item = models.OneToOneField(BaseItem)
    description = models.TextField()
    min_price = models.PositiveIntegerField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def bid(self, hero, bid):
        if not self.valid_to > datetime.datetime.now() > self.valid_from:
            raise Exception()

        new_bid = _Bid(
            hero=hero,
            bid=bid,
            auction_item=self
        )
        new_bid.save()

    def best_bid(self):
        bid = _Bid.objects.filter(auction_item=self).order_by('-bid')[:1]
        if bid.count() > 0:
            return bid[0].bid
        else:
            return self.min_price

    def __unicode__(self):
        return u'%s' % self.item.name


class _Bid(models.Model):
    hero = models.OneToOneField(Hero)
    bid = models.PositiveIntegerField()
    auction_item = models.ForeignKey(AuctionItem)

    def __unicode__(self):
        return u'%s bid %s' % (self.hero, self.bid)