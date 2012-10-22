# coding: utf-8
__author__ = 'Tyr'

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from hero.models import Hero
from django.db import models

class Account(models.Model):
    """
    Użytkownik loguje się używając username i password z modelu User.
    Postać ma inną nazwę, która jest w modelu Hero.
    """
    user = models.OneToOneField(User)

    #Tymczasowy fix, przechodzi testy. W oczekiwaniu na tworzenie bohatera, jak należy.
    hero = models.ManyToManyField(Hero)

    def __unicode__(self):
        return u'Profile of %s' % self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

# to jest w dobrym miejscu? \/
post_save.connect(create_user_profile, sender=User)