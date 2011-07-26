@csrf_exempt
def v_region_list(request, limit=15):
	v_region_list=MyVillage.objects.all()
	northern= MyVillage(v_region='Northern')
	western = MyVillage(v_region='Western')
	uer = MyVillage(v_region='Upper East Region')
	uwr = MyVillage(v_region='Upper West Region')
	central = MyVillage(v_region='Central')
	eastern = MyVillage(v_region='Eastern')
	ga = MyVillage(v_region='Greater Accra')
	ashanti = MyVillage(v_region='Ashanti')
	ba = MyVillage(v_region='Brong Ahafo')
	volta = MyVillage(v_region='Volta Region')
	
	t = loader.get_template('i-kijiji/selectvillage.html')
	c = Context({'region_list':region_list,'user':str(request.user), 'northern':northern, 'western':western, 'uer':uer, 'uwr':uwr, 'central':central, 'eastern':eastern, 'western':western,
	'ga':ga, 'ashanti':ashanti, 'ba':ba, 'volta':volta})
	return HttpResponse(t.render(c))


def v_northern_list(request, limit=15):
	v_northern_list=MyVillage.objects.filter(region='northern').order_by('-v_updated')
	return render_to_response('i-kijiji/v_northern.html', {'v_northern_list': v_northern_list})

def v_uer_list(request, limit=15):
	v_uer_list=MyVillage.objects.filter(region='upper_east').order_by('-v_updated')
	return render_to_response('i-kijiji/v_uer.html', {'v_uer_list': v_uer_list})

def v_uwr_list(request, limit=15):
	v_uwr_list=MyVillage.objects.filter(region='upper_west').order_by('-v_updated')
	return render_to_response('i-kijiji/v_uwr.html', {'v_uwr_list': v_uwr_list})

def v_volta_list(request, limit=15):
	v_volta_list=MyVillage.objects.filter(region='volta').order_by('-v_updated')
	return render_to_response('i-kijiji/v_volta.html', {'v_volta_list': v_volta_list})

def v_central_list(request, limit=15):
	v_central_list=MyVillage.objects.filter(region='central').order_by('-v_updated')
	return render_to_response('i-kijiji/v_central.html', {'v_central_list': v_central_list})

def v_ga_list(request, limit=15):
	v_ga_list=MyVillage.objects.filter(region='greater_accra').order_by('-v_updated')
	return render_to_response('i-kijiji/v_ga.html', {'v_ga_list': v_ga_list})

def v_ba_list(request, limit=15):
	v_ba_list=MyVillage.objects.filter(region='brong_ahafo').order_by('-v_updated')
	return render_to_response('i-kijiji/v_ba.html', {'v_ba_list': v_ba_list})

def v_eastern_list(request, limit=15):
	v_eastern_list=MyVillage.objects.filter(region='eastern').order_by('-v_updated')
	return render_to_response('i-kijiji/v_eastern.html', {'v_eastern_list': v_eastern_list})

def v_western_list(request, limit=15):
	v_western_list=MyVillage.objects.filter(region='western').order_by('-v_updated')
	return render_to_response('i-kijiji/v_western.html', {'v_western_list': v_western_list})

def v_ashanti_list(request, limit=15):
	v_ashanti_list=MyVillage.objects.filter(region='ashanti').order_by('-v_updated')
	return render_to_response('i-kijiji/v_ashanti.html', {'v_ashanti_list': v_ashanti_list})
