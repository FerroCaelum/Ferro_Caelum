from django import forms
import django
from django.forms.models import ModelForm
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')