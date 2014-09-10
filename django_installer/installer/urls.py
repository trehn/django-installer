from django.conf.urls import patterns, url

from .views import installer


urlpatterns = patterns('', url(r'^$', installer, name='installer'))
