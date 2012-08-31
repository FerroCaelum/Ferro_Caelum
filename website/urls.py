from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from views import homepage

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
