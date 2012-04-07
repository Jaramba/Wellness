from django.db import models
from django.contrib.auth.models import User

from fields import  *

class Reminder(models.Model):
	pattern = models.CharField(max_length=200)

class Record(models.Model):
	name = models.CharField(max_length=30)
	patient = models.ForeignKey("patient.Patient")
	attachments = models.ManyToManyField("Attachment")
	notes = models.CharField(max_length=2000)
	
	class Meta:
		abstract=True
		
class Attachment(models.Model):
	name = models.CharField(max_length=120)
	file = models.FileField(upload_to="attachments")
	date_of_upload = models.DateTimeField(auto_now_add=True)

class Person(models.Model):
	'''
	Not Everyone is a patient
	'''
	TITLES = (
		('mr','Mr.'),
		('mrs','Mrs.'),
		('miss','Miss'),
		('dr', 'Dr.'),
		('prof', 'Professor'),
	)
	GENDER = (
		('male', 'Male'),
		('female', 'Female')
	)
	
	title = models.CharField(max_length=20, choices=TITLES, null=True)
	
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=30)
	
	mobile_phone = models.CharField(max_length=50, null=True, blank=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)
	work_phone = models.CharField(max_length=50, null=True, blank=True)

	postal_address = models.CharField(max_length=50, null=True, blank=True)
	photo = models.ImageField(upload_to='photos', null=True, blank=True)
	gender = models.CharField(max_length=20, choices=GENDER, null=True)

	country = CountryField()
	nationality = models.CharField(max_length=150, default='kenyan', null=True)
	
	date_edited = models.DateTimeField(auto_now_add=True)
	date_created = models.DateTimeField(auto_now=True)

class UserProfile(Person):
	user = models.ForeignKey('auth.User', unique=True, null=True)
	
	def __unicode__(self):
		return "%s's profile" % self.user.full_name

#User Hacks...
User.is_healthworker = property(lambda self: self.groups.filter(name='Health workers').count())
User.is_employer = property(lambda self: self.groups.filter(name='Employers').count())
User.is_insuranceprovider = property(lambda self: self.groups.filter(name='Insurance agents').count())

User.full_name = property(lambda self: u' '.join([i for i in (
			(self.profile.get_title_display() if self.profile.title else ''),
			self.first_name,
			(self.profile.middle_name if self.profile.middle_name else ''),
			self.last_name
		) if i
	]
))
User.get_full_name = lambda self: self.full_name
User.__unicode__ = lambda self: self.full_name if self.full_name.split() else self.username

def model_setter(object, name, value, save=True):
	setattr(object, name, value)
	if save: object.save()

#Names; Django form sucks...
get_first_name	= lambda self: self.profile.first_name
set_first_name 	= lambda self, value: model_setter(self.profile, 'first_name', value)
get_middle_name	= lambda self: self.profile.middle_name
set_middle_name	= lambda self, value: model_setter(self.profile, 'middle_name', value)
get_last_name 	= lambda self: self.profile.last_name
set_last_name 	= lambda self, value: model_setter(self.profile, 'last_name', value)

User.first_name = property(get_first_name, set_first_name)
User.middle_name = property(get_middle_name, set_middle_name)
User.last_name = property(get_last_name, set_last_name)

@property
def get_profile(self):
	profile = UserProfile.objects.get_or_create(user=self)[0]
#	if self.is_healthprovider:
#		healthworker = HealthWorker.objects.get(user=self)
	return profile
User.profile = get_profile
