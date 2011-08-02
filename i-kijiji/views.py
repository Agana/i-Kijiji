from django.template import Context, loader
from django.http import HttpResponse
from models import *
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.core.files.uploadedfile import SimpleUploadedFile

def site_list(request, limit=15):
	site_list=TouristSite.objects.all()
	type_hotel = TouristSite(site_type='Hotel')
	type_park = TouristSite(site_type='Park')
	type_forest_reserve = TouristSite(site_type='Forest Reserve')
	type_wetland = TouristSite(site_type='Wetland')
	type_heritage_site = TouristSite(site_type='Heritage Site')
	type_castle = TouristSite(site_type='Fort/Castle')
	type_museum = TouristSite(site_type='Museum')
	
	t = loader.get_template('i-kijiji/sitelist.html')
	c = Context({'site_list':site_list,'user':str(request.user), 'type_hotel':type_hotel, 'type_park':type_park, 		'type_forest_reserve':type_forest_reserve, 'type_wetland':type_wetland, 'type_heritage_site':type_heritage_site, 'type_castle':type_castle, 		'type_museum':type_museum})
	return HttpResponse(t.render(c))

# For Villages

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
	c = Context({'v_region_list':v_region_list,'user':str(request.user), 'northern':northern, 'western':western, 'uer':uer, 'uwr':uwr, 'central':central, 'eastern':eastern, 'western':western,
	'ga':ga, 'ashanti':ashanti, 'ba':ba, 'volta':volta})
	return HttpResponse(t.render(c))


def v_northern_list(request, limit=15):
	v_northern_list=MyVillage.objects.filter(v_region='northern').order_by('-v_updated')
	return render_to_response('i-kijiji/v_northern.html', {'v_northern_list': v_northern_list})

def v_uer_list(request, limit=15):
	v_uer_list=MyVillage.objects.filter(v_region='upper_east').order_by('-v_updated')
	return render_to_response('i-kijiji/v_uer.html', {'v_uer_list': v_uer_list})

def v_uwr_list(request, limit=15):
	v_uwr_list=MyVillage.objects.filter(v_region='upper_west').order_by('-v_updated')
	return render_to_response('i-kijiji/v_uwr.html', {'v_uwr_list': v_uwr_list})

def v_volta_list(request, limit=15):
	v_volta_list=MyVillage.objects.filter(v_region='volta').order_by('-v_updated')
	return render_to_response('i-kijiji/v_volta.html', {'v_volta_list': v_volta_list})

def v_central_list(request, limit=15):
	v_central_list=MyVillage.objects.filter(v_region='central').order_by('-v_updated')
	return render_to_response('i-kijiji/v_central.html', {'v_central_list': v_central_list})

def v_ga_list(request, limit=15):
	v_ga_list=MyVillage.objects.filter(v_region='greater_accra').order_by('-v_updated')
	return render_to_response('i-kijiji/v_ga.html', {'v_ga_list': v_ga_list})

def v_ba_list(request, limit=15):
	v_ba_list=MyVillage.objects.filter(v_region='brong_ahafo').order_by('-v_updated')
	return render_to_response('i-kijiji/v_ba.html', {'v_ba_list': v_ba_list})

def v_eastern_list(request, limit=15):
	v_eastern_list=MyVillage.objects.filter(v_region='eastern').order_by('-v_updated')
	return render_to_response('i-kijiji/v_eastern.html', {'v_eastern_list': v_eastern_list})

def v_western_list(request, limit=15):
	v_western_list=MyVillage.objects.filter(v_region='western').order_by('-v_updated')
	return render_to_response('i-kijiji/v_western.html', {'v_western_list': v_western_list})

def v_ashanti_list(request, limit=15):
	v_ashanti_list=MyVillage.objects.filter(v_region='ashanti').order_by('-v_updated')
	return render_to_response('i-kijiji/v_ashanti.html', {'v_ashanti_list': v_ashanti_list})

# For Tourist Sites

@csrf_exempt
def region_list(request, limit=15):
	region_list=TouristSite.objects.all()
	northern= TouristSite(region='Northern')
	western = TouristSite(region='Western')
	uer = TouristSite(region='Upper East Region')
	uwr = TouristSite(region='Upper West Region')
	central = TouristSite(region='Central')
	eastern = TouristSite(region='Eastern')
	ga = TouristSite(region='Greater Accra')
	ashanti = TouristSite(region='Ashanti')
	ba = TouristSite(region='Brong Ahafo')
	volta = TouristSite(region='Volta Region')
	
	t = loader.get_template('i-kijiji/selectsite.html')
	c = Context({'region_list':region_list,'user':str(request.user), 'northern':northern, 'western':western, 'uer':uer, 'uwr':uwr, 'central':central, 'eastern':eastern, 'western':western,
	'ga':ga, 'ashanti':ashanti, 'ba':ba, 'volta':volta})
	return HttpResponse(t.render(c))


def northern_list(request, limit=15):
	northern_list=TouristSite.objects.filter(region='northern').order_by('-last_modified')
	return render_to_response('i-kijiji/northern.html', {'northern_list': northern_list})

def uer_list(request, limit=15):
	uer_list=TouristSite.objects.filter(region='upper_east').order_by('-last_modified')
	return render_to_response('i-kijiji/uer.html', {'uer_list': uer_list})

def uwr_list(request, limit=15):
	uwr_list=TouristSite.objects.filter(region='upper_west').order_by('-last_modified')
	return render_to_response('i-kijiji/uwr.html', {'uwr_list': uwr_list})

def volta_list(request, limit=15):
	volta_list=TouristSite.objects.filter(region='volta').order_by('-last_modified')
	return render_to_response('i-kijiji/volta.html', {'volta_list': volta_list})

def central_list(request, limit=15):
	central_list=TouristSite.objects.filter(region='central').order_by('-last_modified')
	return render_to_response('i-kijiji/central.html', {'central_list': central_list})

def ga_list(request, limit=15):
	ga_list=TouristSite.objects.filter(region='greater_accra').order_by('-last_modified')
	return render_to_response('i-kijiji/ga.html', {'ga_list': ga_list})

def ba_list(request, limit=15):
	ba_list=TouristSite.objects.filter(region='brong_ahafo').order_by('-last_modified')
	return render_to_response('i-kijiji/ba.html', {'ba_list': ba_list})

def eastern_list(request, limit=15):
	eastern_list=TouristSite.objects.filter(region='eastern').order_by('-last_modified')
	return render_to_response('i-kijiji/eastern.html', {'eastern_list': eastern_list})

def western_list(request, limit=15):
	western_list=TouristSite.objects.filter(region='western').order_by('-last_modified')
	return render_to_response('i-kijiji/western.html', {'western_list': western_list})

def ashanti_list(request, limit=15):
	ashanti_list=TouristSite.objects.filter(region='ashanti').order_by('-last_modified')
	return render_to_response('i-kijiji/ashanti.html', {'ashanti_list': ashanti_list})

def login(request, limit=15):
	#login=TouristSite.objects.filter(region='ashanti').order_by('-last_modified')
	return render_to_response('i-kijiji/login.html')

def register(request, limit=15):
	#login=TouristSite.objects.filter(region='ashanti').order_by('-last_modified')
	return render_to_response('i-kijiji/register.html')

def welcome(request, limit=15):
	
	return render_to_response('i-kijiji/welcome.html')



class SiteForm(ModelForm):
	class Meta:
		exclude=['review_title','review_author']
		model=Review
	def revform(self):
		print review
		return self.fields

class UploadedFileForm(ModelForm):
	class Meta:
		model=MyVillage
	def village_form(self):
		return self.fields
@csrf_exempt
def site_detail(request, id, showReviews=False):
	site_detail=TouristSite.objects.get(id=id)
	site_detail_iterable=TouristSite.objects.filter(id=id)
	review_items=Review.objects.filter(review_title__id=id).order_by('-review_updated')[:3]
	if showReviews:
		
		reviews = Review.objects.filter(review_title__id=id)
		print reviews
	if request.method == 'POST':
		review = Review(review_title=site_detail)
		form = SiteForm(request.POST, instance=review)
		if request.user.is_authenticated:
			review.review_author = request.user.username
		if form.is_valid():
			form.save()
			print form
			return HttpResponseRedirect(request.path)
	else:
		
		form = SiteForm()

	feature_list=MyVillage.objects.all().order_by('?')[:5]
	top_villages=MyVillage.objects.all().order_by('-v_updated')[:5]

	return render_to_response('i-kijiji/sitedetail.html', {'request':request, 'site_detail':site_detail, 'site_detail_iterable':site_detail_iterable, 'review_items':review_items, 'form':form.as_p(), 'feature_list':feature_list, 'top_villages':top_villages})


@csrf_exempt
def village_detail(request, id, showReviews=False):
	village_detail=MyVillage.objects.get(id=id)
	village_detail_iterable=MyVillage.objects.filter(id=id)
	v_review_items=Review.objects.filter(review_title__id=id).order_by('-review_updated')
	if showReviews:
		
		v_reviews = Review.objects.filter(review_title__id=id)
		print reviews
	if request.method == 'POST':
		v_review = Review(review_title=village_detail)
		form = SiteForm(request.POST, instance=review)
		if request.user.is_authenticated:
			v_review.review_author = request.user.username
		if form.is_valid():
			form.save()
			print form
			return HttpResponseRedirect(request.path)
	else:
		
		form = SiteForm()

	feature_list=MyVillage.objects.all().order_by('?')[:5]
	top_villages=MyVillage.objects.all().order_by('-v_updated')[:5]

	return render_to_response('i-kijiji/villagedetail.html', {'request':request, 'village_detail':village_detail, 'village_detail_iterable':village_detail_iterable, 'v_review_items':v_review_items, 'form':form.as_p(), 'feature_list':feature_list, 'top_villages':top_villages})



@csrf_exempt
def my_village(request, limit=15):
	village_myform= MyVillage.objects.all().order_by('-v_updated')
	if request.method == 'POST':
		form = UploadedFileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			#MyDonate.objects.create(first_name='first_name',last_name='last_name', country='country', state='state', city='city', phone='0244', confirm_code='confirm_code')
			return render_to_response('i-kijiji/selectvillage.html', {'request':request, 'village_myform':village_myform})  
	else:
		form = UploadedFileForm()
	 
	return render_to_response('i-kijiji/myvillage.html', {'form': form.as_p(), 'request':request, 'village_myform':village_myform})

#return render_to_response('i-kijiji/myvillage.html', {'request':request, 'my_village':my_village,  'my_village_iterable':my_village_iterabble,  'villages':villages, 'village_items':village_items, 'v_form':v_form.as_p()})





@csrf_exempt
def detail_review(request, id, limit=15, showReviews=False):
	
	
	if showReviews:
		editreview = Review.objects.get(id=id)
		print editreview
	if request.method == 'POST':
		form = SiteForm(request.POST, instance=editreview)
		
		
		if form.is_valid():
			form.save()
			print form
			return HttpResponseRedirect('/i-kijiji/sitedetail/'+ str(editreview.review_title.id)+'/True')
	else:
		form = SiteForm(instance=editreview)

	return render_to_response('i-kijiji/reviewsite.html', {'editreview':editreview, 'request':request, 'site_detail': site_detail, 'user':str(request.user)})

def feature_list(id):
	feature_list=MyVillage.objects.all().order_by('?')[:5]
	#v_features = [feature_list][:5]
	return render_to_response('i-kijiji/features.html', {'feature_list':feature_list})


def feature_list(id):
	#feature_list=MyVillage.objects.all().order_by('?')[:5]
	#v_features = [feature_list][:5]
	return render_to_response('i-kijiji/features.html', {'feature_list':feature_list})

def index(request):
	t = loader.get_template('i-kijiji/index.html')
	c = Context({'site_list':site_list,'user':str(request.user)})
	return HttpResponse(t.render(c))
