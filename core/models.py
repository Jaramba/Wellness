from django.db import models, transaction
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
	date_of_upload = models.DateTimeField(auto_now=True)

class MetaData(models.Model):
	name = models.CharField(max_length=120)
	description = models.CharField(max_length=500)
	date_created = models.DateTimeField(auto_now=True)
	date_changed = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		abstract=True
		
class RelationshipType(MetaData):
	a_is_to_b = models.CharField(max_length=50)
	b_is_to_a = models.CharField(max_length=50)
	weight = models.SmallIntegerField(default=0)
	preffered = models.BooleanField(default=False)

class Relationship(models.Model):
	'''
	A patient can decide to add family and track their files;
	Only this patient can then decide to give access to HealthWorkers
	Only When the PatientKin has reached 18, will they be given access to this system; 
	Registration claim
	----------------
	A patient may state the Emergency Contact to be someone who is not a user of the system,
	Also, they may be just someone they entrust to be their for them on health issues, even 
	their lawyer. So, lets just use any person who can later be a patient. 
	'''
	person_a = models.ForeignKey('Person', related_name='person_a')
	person_b = models.ForeignKey('Person', related_name='person_b')
	next_of_kin = models.BooleanField(default=False)
	relationship = models.ForeignKey(RelationshipType)
	emergency_contact = models.BooleanField(default=False)
	
	@transaction.commit_on_success
	def save(self, force_insert=False, force_update=False):
		if self.patient_id and self.kin_id and (self.kin_id == self.patient_id):
			class CircularRelationException(Exception):pass
			raise CircularRelationException('Sorry. You cannot set yourself as a relation')
		else:
			super(Relationship, self).save(force_insert, force_update)

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
	
	relationship = models.ManyToManyField(
		'self',
		through='Relationship', 
		symmetrical=False, 
	)

	first_name = models.CharField(max_length=50, null=True)
	middle_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	
	mobile_phone = models.CharField(max_length=50, null=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)
	work_phone = models.CharField(max_length=50, null=True, blank=True)

	photo = models.ImageField(upload_to='photos', null=True, blank=True)

	village = models.CharField(max_length=50, null=True, blank=True)
	province = models.CharField(max_length=50, null=True, blank=True)
	postal_code = models.CharField(max_length=50, null=True, blank=True)
	home_address = models.CharField(max_length=50, null=True, blank=True)
	county = models.CharField(max_length=50, null=True, blank=True)
	country = CountryField()
	latitude = models.CharField(max_length=50, null=True, blank=True)
	longitude = models.CharField(max_length=50, null=True, blank=True)
	
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
		return self.full_name
	
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
