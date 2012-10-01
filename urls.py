
from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import Homepage


urlpatterns = patterns('',
    url(r'^$', Homepage.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    (r'^register/$', 'account.views.AccountRegistration')
)