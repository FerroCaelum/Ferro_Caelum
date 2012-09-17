# coding: utf-8
from django.db import models

class Ability(models.Model):
    """Reprezentuje zdolność aktywowaną przez bohatera podczas walki."""
    name = models.CharField(max_length=50)
    last = models.PositiveSmallIntegerField()
