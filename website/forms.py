from django import forms

class SignUpForm(forms.Form):
    login = forms.CharField()
    email=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)