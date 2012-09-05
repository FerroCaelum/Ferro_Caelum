# coding: utf-8
__author__ = 'episage'

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from forms import CreateAccountForm

class CreateAccount(CreateView):
    template_name = "account/create.html"
    form_class = CreateAccountForm


class CreateSuccess(TemplateView):
    template_name = 'account/create-success.html'
