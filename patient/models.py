from django.db import models
from core.models import *
from django.contrib.auth.models import User

class EmergencyContact(models.Model):
	RELATIONSHIPS = [
	]
	
	patient = models.ForeignKey('Patient', related_name='patient')
	contact = models.ForeignKey('auth.User', related_name='contact')
	relationship = models.CharField(max_length=50, choices=RELATIONSHIPS)
	send_text = models.BooleanField(default=False)
	detailed_message = models.BooleanField(default=False)

class Patient(Person):
	MEDICATION_TYPE=[]

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
	SMOKE_TYPE = [
	]
	SMOKER_TYPE = [
	]
	DRINKER_TYPE = [
	]
	DRINK_TYPE = [
	]	
	EXCERCISE_FREQUENCY=[
	]
	DIET_TYPE=[
	]
	date_of_birth = models.DateField(null=True)

	user = models.ForeignKey('auth.User', unique=True, related_name='patient_user')
	next_of_kin = models.ForeignKey('auth.User', related_name='next_of_kin')
	emergency_contacts = models.ManyToManyField('auth.User', through='EmergencyContact', related_name='contacts')
	
	blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS)
	weight = models.PositiveSmallIntegerField(default=0)
	height = models.PositiveSmallIntegerField(default=0)
	
	#smokers
	smoking = models.CharField(max_length=100, choices=SMOKER_TYPE)
	smoker_type = models.CharField(max_length=100, choices=SMOKE_TYPE,help_text='')
	duration_smoking = models.PositiveSmallIntegerField(help_text='Number of years smoking')
	
	#drinkers
	drinking = models.CharField(max_length=100, choices=DRINKER_TYPE)
	drinker_type = models.CharField(max_length=100, choices=DRINK_TYPE, help_text='')
	duration_drinking = models.PositiveSmallIntegerField(help_text='Number of years drinking')
	
	#Exercise
	excercising_times = models.PositiveSmallIntegerField(help_text='Number of years')
	excercise_frequency = models.CharField(max_length=100, choices=EXCERCISE_FREQUENCY, help_text='')
	diet = models.CharField(max_length=100, choices=DIET_TYPE, help_text='')

	family_cancer_status = models.BooleanField(default=False)
	cancer_type = models.CharField(max_length=50)	

	other_diseases = models.BooleanField(default=False)

	disabilities = models.CharField(max_length=250)

	insurance = models.ManyToManyField('insuranceprovider.Insurance', through='insuranceprovider.PatientInsurance')

	personal_doctor = models.ForeignKey('healthprovider.HealthWorker')
	medication = models.CharField(max_length=100, choices=MEDICATION_TYPE, help_text='')
	last_doctor_visit = models.DateTimeField()
		
@property
def get_profile(self):
	profile = Patient.objects.get_or_create(user=self)[0]
	if self.is_employer:
		profile = ''
	return profile
		
User.profile = get_profile