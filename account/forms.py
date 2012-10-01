from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from account.models import Account


class RegistrationForm(ModelForm):
    username    = forms.CharField(label = (u'User Name'))
    email       = forms.EmailField(label=(u'Email Address'))
    password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password_re = forms.CharField(label=(u'Verify Password'),widget=forms.PasswordInput(render_value=False))
    #age
    #sex
    class Meta:
        model = Account
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Occupado")

    def clean(self):
        password = self.cleaned_data.get('password', None)
        password_re = self.cleaned_data.get('password_re', None)
        if password != password_re:
            raise forms.ValidationError("Haslo niezgodne z polem do jego konfirmacji")
        return self.cleaned_data

