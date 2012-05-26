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
	
	patient_number = models.CharField(unique=True, max_length=15)
	
	gender = models.CharField(max_length=20, choices=GENDER, null=True)
	date_of_birth = models.DateField(null=True)
	
	blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS, null=True)
	weight = models.PositiveSmallIntegerField(default=0, null=True)
	height = models.PositiveSmallIntegerField(default=0, null=True)
	
	employer 	= models.ForeignKey('insuranceprovider.EmployerCompany', null=True)
	insurance	= models.ManyToManyField('insuranceprovider.Insurance', through='insuranceprovider.PatientInsurance')

	last_doctor_visit = models.DateTimeField(null=True)
	
	def __unicode__(self):
		return '%s [PNo. %s]' % (self.full_name, self.patient_number)
	