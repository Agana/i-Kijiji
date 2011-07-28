from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from reg.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'users.views.loginView'),
    url(r'^logout/$', 'users.views.logoutView'),
)
