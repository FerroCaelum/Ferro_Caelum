from django.conf.urls import patterns, url

urlpatterns = patterns('hero.views',
    url(r'^$', 'index'),
)
