from django.db import models
from core.models import *

from insuranceprovider.models import *

class HealthCareFacility(EmployerCompany):
	TYPES = []
	type = models.CharField(max_length=50, choices=TYPES)
	speciality = models.CharField(max_length=200)

class HealthWorker(Person):
	user = models.ForeignKey('auth.User', unique=True, related_name='health_user')
	speciality = models.CharField(max_length=200)
	