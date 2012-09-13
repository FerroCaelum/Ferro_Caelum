from django.conf.urls import patterns, include, url
from django.contrib import admin
from hero.views import *
from views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Homepage.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sign-up/', SignUpView.as_view()),
    url(r'^hero/', include('hero.urls')),
)
