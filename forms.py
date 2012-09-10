from django import forms
import django
from django.forms.models import ModelForm
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
    class Meta:
        model=User
        fields=('login','password',)
    login = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)