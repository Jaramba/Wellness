from uhai.core.models import *
from uhai.core.utils import pkgen
from uhai.userprofile.models import *

from django.contrib.auth.models import User
from django.db import models, transaction

from uhai.healthprovider.models import HealthWorker

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
	date_of_birth = models.DateField(null=True, help_text='The Patient\'s indicated date of birth')
	
	blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS, null=True)
	weight = models.CharField(max_length=5, default=0, null=True, help_text='Enter weight in Kilograms (Kgs)')
	height = models.CharField(max_length=7, default=0, null=True, help_text='Enter standard height, eg: 5\'9" for 5 foot 9 inch')
	
	employer  = models.ForeignKey('insuranceprovider.EmployerCompany', null=True)
	insurance = models.ManyToManyField('insuranceprovider.Insurance', through='insuranceprovider.PatientInsurance')
	
	def __unicode__(self):
		return '%s [PNo. %s]' % (self.full_name, self.patient_number)
	
	class Meta:
		permissions = ( 
		    ('view_patient', 'View patient'), 
		)