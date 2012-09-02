from django import forms
import django
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from hero import models
class NewAccountForm(ModelForm):
    class Meta:
        model=User
#        fields=('username','password')
#    login = forms.CharField()
#    email = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)