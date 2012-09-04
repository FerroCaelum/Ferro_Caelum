from django.db.models.signals import post_save

__author__ = 'Tyr'
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    #birthday = models.DateField
    real_name = models.CharField(max_length=50)

    #providuje get_profile() - bedzie zwracac account. W krytycznym przypadku zmienic user.username na real_name
    # pomysl - real_name to nazwa postaci, np inna niz nazwa logowania
    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)