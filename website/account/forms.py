# coding: utf-8
__author__ = 'episage'

from django.forms.models import ModelForm
from django.contrib.auth.models import User

class CreateAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')