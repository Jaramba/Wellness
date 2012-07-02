from django.db import models, transaction
from django.contrib.auth.models import User, Group
from django.db import models

class OwnerModel(models.Model):
	owner = models.ForeignKey('auth.User', null=True, editable=False)
	
	class Meta:
		abstract = True

class Record(models.Model):
	name = models.CharField(max_length=30)
	patient = models.ForeignKey("patients.Patient")
	notes = models.TextField()
	
	class Meta:
		abstract=True

class MetaData(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now=True)
	date_changed = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		abstract=True

class Country(models.Model):
	name = models.CharField(max_length=150)
	iso = models.CharField(max_length=4)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Countries'
		pass#sort = ['name']
		
class Province(models.Model):
	name = models.CharField(max_length=150)
	iso = models.CharField(max_length=4)
	country = models.ForeignKey(Country)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Provinces'
		
class County(models.Model):
	name = models.CharField(max_length=150)
	iso = models.CharField(max_length=4)
	province = models.ForeignKey(Province)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Counties'
		pass#sort = ['name']
			