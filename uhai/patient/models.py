from uhai.core.models import *
from uhai.core.utils import pkgen
from uhai.userprofile.models import *

from django.contrib.auth.models import User
from django.db import models, transaction

from uhai.healthprovider.models import HealthWorker

class Patient(models.Model):
	GENDER = (
		('male', 'Male'),
		('female', 'Female')
	)
	DIET_TYPE=[]
	BLOOD_GROUPS = [
		('a-positive','A+'),
		('a-negative','A-'),
		('b-positive','B+'),
		('b-negative','B-'),
		('ab-positive','AB+'),
		('ab-negative','AB-'),
		('o-positive','O+'),
		('o-negative','O-'),
	]

	patient_number = models.CharField(primary_key=True, unique=True, max_length=15)
	user = models.OneToOneField('auth.User')

	relationship = models.ManyToManyField(
		'userprofile.Person',
		related_name='patient_relationship',
		through='patient.Relationship',
		symmetrical=False,
	)

	gender = models.CharField(max_length=20, choices=GENDER, null=True)
	date_of_birth = models.DateField(null=True, help_text='The Patient\'s indicated date of birth')

	blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS, null=True)
	weight = models.CharField(max_length=5, default=0, null=True, help_text='Enter weight in Kilograms (Kgs)')
	height = models.CharField(max_length=7, default=0, null=True, help_text='Enter standard height, eg: 5\'9" for 5 foot 9 inch')

	employer  = models.ForeignKey('insuranceprovider.EmployerCompany', null=True)
	insurance = models.ManyToManyField('insuranceprovider.Insurance', through='insuranceprovider.PatientInsurance')

	def __unicode__(self):
		return '[PNo. %s]' % (self.patient_number)
	
	class Meta:
		permissions = ( 
		    ('view_patient', 'View patient'), 
		)
		verbose_name_plural = 'Patient Profile'
		
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
	person_a = models.ForeignKey('Patient', verbose_name='Patient', related_name='person_a')
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
