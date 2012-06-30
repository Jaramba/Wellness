from django.db import models
from uhai.core.models import *
from uhai.userprofile.models import *
from uhai.insuranceprovider.models import *

class SpecialityCategory(models.Model):
	name = models.CharField(max_length=150)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Speciality Categories'

class Speciality(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, unique=True)
	category = models.ForeignKey(SpecialityCategory, null=True, blank=True)
	date_added = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s (%s)' % (self.name, self.category)

	class Meta:
		verbose_name_plural = 'Specialities'

class HealthCareFacility(Company):
	official_hospital_number = models.CharField(max_length=20, null=True, blank=False)
	speciality = models.ManyToManyField(Speciality)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Health care facilities'
        permissions = (
            ('view_healthcarefacility', 'View health care facility'),
        )

class HealthWorker(models.Model):
	user = models.OneToOneField('auth.User')
	facility = models.ForeignKey(HealthCareFacility)
	speciality = models.ManyToManyField(Speciality)
	practice_number = models.CharField(max_length=20, null=True, blank=False)

	def __unicode__(self):
		return self.practice_number
	
	class Meta:
		permissions = (
			('view_healthworker', 'View health worker'),
		)
		verbose_name_plural = 'Health Worker Profile'
