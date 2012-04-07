from core.models import *
from core.utils import pkgen

from django.contrib.auth.models import User
from django.db import models, transaction

from healthprovider.models import HealthWorker

RELATIONSHIPS = [
	('brother', 'Brother'),
	('sister', 'Sister'),
	('son', 'Son'),
	('daughter', 'Daughter'),
	('aunt', 'Aunt'),
	('uncle', 'Uncle'),
	('niece', 'Niece'),
	('nephew', 'Nephew'),
	('cousin', 'Cousin'),
	('spouse', 'Spouse'),
	('grandfather', 'Grandfather'),
	('grandmother', 'Grandmother'),
]

class PatientKin(models.Model):
	'''
	A patient can decide to add family and track their files;
	Only this patient can then decide to give access to HealthWorkers
	Only When the PatientKin has reached 18, will they be given access to this system; 
	Registration claim
	'''
	patient = models.ForeignKey('Patient', related_name='patient')
	kin = models.ForeignKey('Patient', related_name='patient_kin')
	next_of_kin = models.BooleanField(default=False)
	relationship = models.CharField(max_length=50, choices=RELATIONSHIPS)
	emergency_contact = models.BooleanField(default=False)
	
	@transaction.commit_on_success
	def save(self, force_insert=False, force_update=False):
		if self.patient and self.kin and (self.kin.id == self.patient.id):
			class CircularRelationException(Exception):pass
			raise CircularRelationException('Sorry. You cannot set yourself as your own kin')
		else:
			super(Patient, self).save(force_insert, force_update)

class EmergencyContact(models.Model):
	'''
	A patient may state the Emergency Contact to be someone who is not a user of the system,
	Also, they may be just someone they entrust to be their for them on health issues, even 
	their lawyer. So, lets just use any person who can later be a patient. 
	'''
	contact = models.ForeignKey('core.Person')
	patient = models.ForeignKey('Patient', related_name='patient_contact')
	relationship = models.CharField(max_length=50, choices=RELATIONSHIPS)
	send_text = models.BooleanField(default=False)
	detailed_message = models.BooleanField(default=False)

class Patient(models.Model):
	'''
	A patient with auth.User field empty is thought to have been under guardianship.
	thus, they will inherit the nearest family members' doctor and entrustment
	Everyone is a patient, and or whoever they choose to be.
	'''
	SMOKE_TYPE = []
	SMOKER_TYPE = []
	DRINKER_TYPE = []
	DRINK_TYPE = []
	EXCERCISE_FREQUENCY=[]
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
	
	profile = models.ForeignKey(UserProfile)
	date_of_birth = models.DateField(null=True)
	
	kins = models.ManyToManyField('Patient', null=True, through='PatientKin', related_name='patient_kins')
	emergencycontacts = models.ManyToManyField('core.Person', null=True, through='EmergencyContact', related_name='patient_emergencycontacts')
	
	blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS)
	weight = models.PositiveSmallIntegerField(default=0, null=True)
	height = models.PositiveSmallIntegerField(default=0, null=True)
	
	#smokerspersonal_doctor
	smoking = models.CharField(max_length=100, null=True, blank=True, choices=SMOKER_TYPE)
	smoker_type = models.CharField(max_length=100, null=True, blank=True, choices=SMOKE_TYPE,help_text='')
	duration_smoking = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Number of years smoking')
	
	#drinkers
	drinking = models.CharField(null=True, blank=True, max_length=100, choices=DRINKER_TYPE)
	drinker_type = models.CharField(max_length=100, null=True, blank=True, choices=DRINK_TYPE, help_text='')
	duration_drinking = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Number of years drinking')
	
	#Exercise
	excercising_times = models.PositiveSmallIntegerField(null=True, blank=True, help_text='Number of years')
	excercise_frequency = models.CharField(max_length=100, choices=EXCERCISE_FREQUENCY, null=True, blank=True, help_text='')
	diet = models.CharField(max_length=100, choices=DIET_TYPE, null=True, blank=True, help_text='')

	family_cancer_status = models.BooleanField(default=False)
	cancer_type = models.CharField(max_length=50, null=True, blank=True)	

	other_diseases = models.BooleanField(default=False)
	disabilities = models.CharField(max_length=250, null=True, blank=True)

	employer = models.ForeignKey('insuranceprovider.EmployerCompany')
	
	insurance	= models.ManyToManyField('insuranceprovider.Insurance', through='insuranceprovider.PatientInsurance')
	medications	= models.ManyToManyField('medication.Medication', through='medication.Prescription')

	doctor = models.ForeignKey('healthprovider.HealthWorker', null=True, related_name='physician')
	last_doctor_visit = models.DateTimeField(null=True)
	
	def __unicode__(self):
		return self.profile.full_name
	