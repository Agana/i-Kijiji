from django.contrib import admin

from django.db import models

from django.db import models

class TouristSite(models.Model):
	name= models.CharField(max_length=200)
	town= models.CharField(max_length=200)
	country= models.CharField(max_length=200)
	last_modified= models.DateTimeField(auto_now=True)
	SITE_CHOICES=(('hotel', 'Hotel'), ('park', 'Park'), ('forest_reserve', 'Forest Reserve'), ('wetland', 'Wetland'), ('heritage_site', 'Heritage Site'),('castle','Fort/Castle'),('museum', 'Museum'))
	site_type=models.CharField(max_length=60, choices=SITE_CHOICES)
	REGION_CHOICES=(('greater_accra', 'Greater Accra'), ('northern', 'Northern'), ('brong_ahafo', 'Brong Ahafo'),
	('central', 'Central'), ('upper_east', 'Upper East'),
	('upper_west','Upper West'),('ashanti', 'Ashanti'),('volta','Volta'),('western', 'Western'),('eastern', 'Eastern'))
	region= models.CharField(max_length=60, choices=REGION_CHOICES)
	def __unicode__(self):
		return self.name


class Review(models.Model):
	review_title = models.ForeignKey('TouristSite')
	review_body= models.TextField()
	review_author= models.CharField(max_length=60)
	review_created= models.DateTimeField(auto_now=True)
	review_updated= models.DateTimeField(auto_now_add=True)
	def title_first_ten(self):
		return self.title[:10]
        def __unicode__(self):
		return self.review_author
	
class MyVillage(models.Model):
	v_name= models.CharField('Village name', max_length=30)
	v_region= models.CharField('Region', max_length=30)
	v_nearto= models.CharField('Nearest city/town', max_length=30)
	v_attraction1= models.CharField('Attraction 1',max_length=50)
	v_attraction2= models.CharField('Attraction 2',max_length=50)
	v_attraction3= models.CharField('Attraction 3',max_length=50)
	v_attraction4= models.CharField('Attraction 4',max_length=50)
	v_attraction5= models.CharField('Attraction 5',max_length=50)
	v_review= models.TextField('Village Review')
	v_added=models.DateTimeField('Date added', auto_now=True)
	v_updated=models.DateTimeField('Last updated', auto_now_add=True)
	REGION_CHOICES=(('greater_accra', 'Greater Accra'), ('northern', 'Northern'), ('brong_ahafo', 'Brong Ahafo'),
	('central', 'Central'), ('upper_east', 'Upper East'),
	('upper_west','Upper West'),('ashanti', 'Ashanti'),('volta','Volta'),('western', 'Western'),('eastern', 'Eastern'))
	v_region= models.CharField(max_length=60, choices=REGION_CHOICES)
	def __unicode__(self):
		return self.v_name


class ReviewInline(admin.TabularInline):
        model = Review

class TouristSiteAdmin(admin.ModelAdmin):
	list_display = ('name', 'town', 'region', 'last_modified')
	search_fields = ('name', 'region', 'description')
	list_filter = ('name','last_modified')
	inlines = [ReviewInline]


admin.site.register(TouristSite, TouristSiteAdmin)

