# coding: utf-8
from django.db import models
from blood_line.models import BloodLine
from profession.models import Profession

from .owner import Owner

class Hero(Owner):
    blood_line = models.OneToOneField(BloodLine, null=True)
    profession = models.OneToOneField(Profession, null=True)

    exp = models.PositiveIntegerField(default=0)

    energy = models.PositiveIntegerField(default=1)
    max_energy = models.PositiveIntegerField(default=1)
    hp = models.PositiveIntegerField(default=1)
    max_hp = models.PositiveIntegerField(default=1)
    ap = models.PositiveIntegerField(default=1)
    max_ap = models.PositiveIntegerField(default=1)

    def meets_bloodline_requirament(self, talent):
        requirement = talent.blood_line_requirement
        return True if (not requirement) or self.blood_line == requirement else False

    def __unicode__(self):
        return self.name