from django.db import models
from core.models import *

class Hospital(models.Model):
	name = models.CharField(max_length=50)
	health_providers = models.ManyToMany("healthprovider.HealthProvider")
	date_edited = models.DateTimeField(auto_now=True)
	date_added = models.DateTimeField(auto_now_add=True)

class Doctor(Person):
	speciality = models.CharField(max_length=200)
	hospitals = models.ManyToMany("Hospital")
	
