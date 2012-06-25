from django.db import models, transaction
from django.contrib.auth.models import User, Group
from django.db import models

class OwnerModel(models.Model):
	owner = models.ForeignKey('auth.User', null=True, editable=False)

class Record(models.Model):
	name = models.CharField(max_length=30)
	enrollee = models.ForeignKey("patient.Patient")
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
	person_a = models.ForeignKey('userprofile.Person', verbose_name='Patient', related_name='person_a')
	person_b = models.ForeignKey('userprofile.Person', verbose_name='Person', related_name='person_b')
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
			