from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save


__author__ = 'Tyr'
#   obecny problem - polaczenie konta uzytkownika i bohatera.
#   proponowane rozwiazanie - podobnie jak polaczenie user z account - OneToOneField z hero
#   jeden issue - po rejestracji wypadaloby odsylac do tworzenia bohatera. Znow post_save?

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    #hero = models.OneToOneField(models.ForeignKey('hero.Hero'))  #nie mam zielonego pojecia, czy to zadziala.
                                                                  # Ale jak tak, to genialne.
                                                                  #nie zadzialalo. Trzeba zaimportowac,
                                                                  # ale wywala mi bledy
    real_name = models.CharField(max_length=50)



    #   providuje get_profile() - bedzie zwracac account. W krytycznym przypadku zmienic user.username na real_name
    #   pomysl - real_name to nazwa postaci, np inna niz nazwa logowania.
    def __unicode__(self):
        return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)