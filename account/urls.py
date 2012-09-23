# coding: utf-8
__author__ = 'episage'

from django.conf.urls import patterns, include, url
from views import CreateAccount
from views import CreateSuccess

urlpatterns = patterns('',
    url(r'^create/$', CreateAccount.as_view()),
    url(r'^create-success/$', CreateSuccess.as_view()),
)

