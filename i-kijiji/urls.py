from django.conf.urls.defaults import *
from django.contrib import admin


urlpatterns = patterns('',
	url(r'^$', 'i-kijiji.views.welcome'),
	url(r'^sitelist/$', 'i-kijiji.views.site_list'),
	url(r'^selectsite/$', 'i-kijiji.views.region_list'),
	url(r'^northern/$', 'i-kijiji.views.northern_list'),
	url(r'^uer/$', 'i-kijiji.views.uer_list'),
	url(r'^uwr/$', 'i-kijiji.views.uwr_list'),
	url(r'^volta/$', 'i-kijiji.views.volta_list'),
	url(r'^ga/$', 'i-kijiji.views.ga_list'),
	url(r'^ba/$', 'i-kijiji.views.ba_list'),
	url(r'^ashanti/$', 'i-kijiji.views.ashanti_list'),
	url(r'^eastern/$', 'i-kijiji.views.eastern_list'),
	url(r'^western/$', 'i-kijiji.views.western_list'),
	url(r'^central/$', 'i-kijiji.views.central_list'),

	url(r'^sitedetail/(?P<id>\d+)/$','i-kijiji.views.site_detail'),
	
	url(r'^reviewsite/(?P<id>\d+)/((?P<showReviews>.*)/)?$','i-kijiji.views.detail_review'),
	url(r'^login/$', 'i-kijiji.views.login'),	
	url(r'^register/$', 'i-kijiji.views.register'),
	url(r'^welcome/$', 'i-kijiji.views.welcome'),
	url(r'^myvillage/$', 'i-kijiji.views.my_village'),
)
