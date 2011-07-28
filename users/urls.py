from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from users.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'users.views.loginView'),
    url(r'^login/$', 'users.views.loginView'),
    url(r'^logout/$', 'users.views.logoutView'),
    url(r'^register/$', 'users.views.register'),
)
