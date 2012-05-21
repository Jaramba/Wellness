from core.models import *
from core.utils import pkgen

from django.contrib.auth.models import User
from django.db import models, transaction

from healthprovider.models import HealthWorker

class Patient(UserProfile):
	'''
	A patient with auth.User field empty is thought to have been under guardianship.
	thus, they will inherit the nearest family members' doctor and entrustment
	Everyone is a patient, and or whoever they choose to be.
	'''
	GENDER = (
		('male', 'Male'),
		('female', 'Female')
	)
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
	
	gender = models.CharField(max_length=20, choices=GENDER, null=True)
	date_of_birth = models.DateField(null=True)
	
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

	last_doctor_visit = models.DateTimeField(null=True)
	
	def __unicode__(self):
		return self.full_name
	