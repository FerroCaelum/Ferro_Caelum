from django.db import models

__author__ = 'episage'

class BlackMarket(models.Model):
    name = models.CharField(max_length=50)
