from django.db import models, transaction
from django.contrib.auth.models import User
from permission.models import Role

from fields import  *

class Record(models.Model):
	name = models.CharField(max_length=30)
	patient = models.ForeignKey("patient.Patient")
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

class RelationshipType(models.Model):
	a_is_to_b = models.CharField(max_length=50)
	b_is_to_a = models.CharField(max_length=50)
	preffered = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now=True)
	date_changed = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.a_is_to_b + ' - ' + self.b_is_to_a

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
	person_a = models.ForeignKey('Person', verbose_name='Patient', related_name='person_a')
	person_b = models.ForeignKey('Person', verbose_name='Person', related_name='person_b')
	next_of_kin = models.BooleanField(default=False)
	relationship = models.ForeignKey(RelationshipType)
	emergency_contact = models.BooleanField(default=False)
	
	def __unicode__(self):
		return '%s and %s (%s)' % (self.person_a, self.person_b, self.relationship)
	
	@transaction.commit_on_success
	def save(self, force_insert=False, force_update=False):
		if self.person_a_id and self.person_b_id and (self.person_a_id == self.person_b_id):
			class CircularRelationException(Exception):pass
			raise CircularRelationException('Sorry. You cannot set yourself as a relation')
		else:
			super(Relationship, self).save(force_insert, force_update)

class Country(models.Model):
	name = models.CharField(max_length=150)
	iso = models.CharField(max_length=4)
	
	def __unicode__(self):
		return '%s' % (self.name)
	
	class Meta:
		verbose_name_plural = 'Countries'
		pass#sort = ['name']
		
class Province(models.Model):
	name = models.CharField(max_length=150)
	iso = models.CharField(max_length=4)
	country = models.ForeignKey(Country)
	
	def __unicode__(self):
		return '%s, %s' % (self.name, self.country)
	
	class Meta:
		verbose_name_plural = 'Provinces'
		#sort = ['name']
		
class County(models.Model):
	name = models.CharField(max_length=150)
	iso = models.CharField(max_length=4)
	province = models.ForeignKey(Province)
	
	def __unicode__(self):
		return '%s, %s' % (self.name, self.province)
	
	class Meta:
		verbose_name_plural = 'Counties'
		pass#sort = ['name']
			
class Title(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

class Person(models.Model):
	'''
	Not Everyone is a patient; This will act as a staging profile, until someone
	gets an account.... hmmm, should we create an inactive user or just this?
	'''
	title = models.ForeignKey(Title, null=True)
	relationship = models.ManyToManyField(
		'self',
		through='Relationship',
		symmetrical=False,
	)

	first_name = models.CharField(max_length=50, null=True)
	middle_name = models.CharField(max_length=50, null=True, )
	last_name = models.CharField(max_length=50, null=True, help_text="Family/Sur-name")
	
	mobile_phone = models.CharField(max_length=50, null=True, help_text="Format: +2547xxxxxxxx or +254020xxxxxxx")
	home_phone = models.CharField(max_length=50, null=True, blank=True, help_text="Format: +2547xxxxxxxx or +254020xxxxxxx")
	work_phone = models.CharField(max_length=50, null=True, blank=True, help_text="Format: +2547xxxxxxxx or +254020xxxxxxx")

	photo = models.FileField(upload_to='photos', null=True, blank=True)

	postal_code = models.CharField(max_length=50, null=True, blank=True)
	village = models.CharField(max_length=50, null=True, blank=True)
	province = models.ForeignKey(Province, null=True)
	county = models.ForeignKey(County, null=True)
	country = models.ForeignKey(Country, null=True)
	
	latitude = models.CharField(max_length=50, null=True, blank=True, editable=False)
	longitude = models.CharField(max_length=50, null=True, blank=True, editable=False)
	
	date_edited = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.full_name
	
	@property
	def full_name(self):
		return u' '.join([i for i in (
					(self.title.name if self.title else ''),
					self.first_name if hasattr(self, 'first_name') else '',
					(self.middle_name if self.middle_name else ''),
					self.last_name if hasattr(self, 'last_name') else ''
				) if i
			])
	class Meta:
		verbose_name = 'Person'
        permissions = (
            ('view_person', 'View person'),
        )

class UserProfile(Person):
	user = models.OneToOneField('auth.User')
	national_id = models.CharField(max_length=25)
	
	def __unicode__(self):
		return self.full_name
	
	class Meta:
		verbose_name = 'System User profile'
        permissions = (
            ('view_userprofile', 'View User profile'),
        )
	
	@property
	def full_name(self):
		return u' '.join([i for i in (
					(self.title.name if self.title else ''),
					self.first_name,
					(self.middle_name if self.middle_name else ''),
					self.last_name
				) if i
			])

#User Hacks...
User.is_healthworker = property(lambda self: Role.objects.filter(codename='health_worker').count())
User.is_employer = property(lambda self: Role.objects.filter(codename='employers'))
User.is_insuranceprovider = property(lambda self: Role.objects.filter(codename='insurance_agents').count())

User.full_name = property(lambda self: self.profile.full_name)
User.get_full_name = lambda self: self.full_name
User.__unicode__ = lambda self: self.full_name if self.full_name.split() else self.username

def get_profile(self):
	if not hasattr(self, '_profile_cache'):
		self._profile_cache = UserProfile.objects.get_or_create(user=self)[0] if self.pk else None
	return self._profile_cache

User.get_profile = get_profile
User.profile = property(get_profile)
