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
	Not Everyone is a patient; This will act as a staging profile, until someone
	gets an account.... hmmm, should we create an inactive user or just this?
	'''
	TITLES = (
		('mr','Mr.'),
		('mrs','Mrs.'),
		('miss','Miss'),
		('dr', 'Dr.'),
		('prof', 'Professor'),
	)
	title = models.CharField(max_length=20, choices=TITLES, null=True)

	first_name = models.CharField(max_length=50, null=True)
	middle_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	
	mobile_phone = models.CharField(max_length=50, null=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)
	work_phone = models.CharField(max_length=50, null=True, blank=True)

	postal_address = models.CharField(max_length=50, null=True)
	photo = models.ImageField(upload_to='photos', null=True, blank=True)

	country = CountryField()
	nationality = models.CharField(max_length=150, default='kenyan', null=True)
	
	date_edited = models.DateTimeField(auto_now_add=True)
	date_created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.full_name
	
	@property
	def full_name(self):
		return u' '.join([i for i in (
					(self.get_title_display() if self.title else ''),
					self.first_name if hasattr(self, 'first_name') else '',
					(self.middle_name if self.middle_name else ''),
					self.last_name if hasattr(self, 'last_name') else ''
				) if i
			])

class UserProfile(Person):
	user = models.OneToOneField('auth.User')
	
	def __unicode__(self):
		return "%s's profile" % self.user.full_name if self.user else ''
	
	class Meta:
		verbose_name = 'Personal info'
		verbose_name_plural = 'Personal info'
	
	@property
	def full_name(self):
		return u' '.join([i for i in (
					(self.get_title_display() if self.title else ''),
					self.first_name,
					(self.middle_name if self.middle_name else ''),
					self.last_name
				) if i
			])

#User Hacks...
User.is_healthworker = property(lambda self: self.groups.filter(name='Health workers').count())
User.is_employer = property(lambda self: self.groups.filter(name='Employers').count())
User.is_insuranceprovider = property(lambda self: self.groups.filter(name='Insurance agents').count())

User.full_name = property(lambda self: self.profile.full_name)
User.get_full_name = lambda self: self.full_name
User.__unicode__ = lambda self: self.full_name if self.full_name.split() else self.username

def get_profile(self):
	if not hasattr(self, '_profile_cache'):
		self._profile_cache = UserProfile.objects.get_or_create(user=self)[0] if self.pk else None
	return self._profile_cache

User.get_profile = get_profile
User.profile = property(get_profile)
