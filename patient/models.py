from django.db import models
from core.models import *

class Patient(Person):
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
	MEDICATION_TYPE=[]

	next_of_kin = models.CharField(max_length=100, null=True)
	next_of_kin_phone = models.CharField(max_length=15, null=True)
	next_of_kin_email = models.EmailField(max_length=120, null=True)
	next_of_kin_address = models.CharField(max_length=100, null=True)
	
	health_provider = models.ForeignKey("healthprovider.HealthProvider")
	personal_doctor = models.ForeignKey("doctor.Doctor")

	blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS)
	weight = models.PositiveSmallIntegerField(default=0)
	height = models.PositiveSmallIntegerField(default=0)
	
	#smokers
	smoking = models.CharField(max_length=100, choices=SMOKER_TYPE)
	smoker_type = models.CharField(max_length=100, choices=SMOKE_TYPE,help_text="")
	duration_smoking = models.PositiveSmallIntegerField(help_text="Number of years smoking")
	
	#drinkers
	drinking = models.CharField(max_length=100, choices=DRINKER_TYPE)
	drinker_type = models.CharField(max_length=100, choices=DRINK_TYPE, help_text="")
	duration_drinking = models.PositiveSmallIntegerField(help_text="Number of years drinking")
	
	#Exercise
	excercising_times = models.PositiveSmallIntegerField(help_text="Number of years")
	excercise_frequency = models.CharField(max_length=100, choices=EXCERCISE_FREQUENCY, help_text="")
	diet = models.CharField(max_length=100, choices=DIET_TYPE, help_text="")
	medication = models.CharField(max_length=100, choices=MEDICATION_TYPE, help_text="")

	family_cancer_status = models.BooleanField(default=False)
	cancer_type = models.CharField(max_length=50)	

	other_diseases = models.BooleanField(default=False)

	date_of_birth = models.DateField(null=True)

	disabilities = models.CharField(max_length=250)
	disabilities = models.CharField(max_length=250)

	last_doctor_visit = models.DateTimeField()
	
	

