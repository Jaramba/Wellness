from django.db import models
from core.models import *

class Doctor(Person):
	speciality = models.CharField(max_length=200)
	hospitals = models.ManyToManyField("Hospital")

class Hospital(models.Model):
	name = models.CharField(max_length=50)
	insurance_providers = models.ManyToManyField("insuranceprovider.InsuranceProvider")
	date_edited = models.DateTimeField(auto_now=True)
	date_added = models.DateTimeField(auto_now_add=True)

	
