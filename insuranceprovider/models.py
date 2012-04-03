from django.db import models
from records.models import Record

class EmployerCompany(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField()
	location = models.CharField(max_length=200)
	insurance_providers = models.ManyToManyField('HealthInsuranceProvider')
	date_edited = models.DateTimeField(auto_now=True)
	date_added = models.DateTimeField(auto_now_add=True)

class HealthInsuranceProvider(EmployerCompany):pass

class Insurance(models.Model):
	TYPES = [
		('health', 'Health'),
		('dental', 'Dental'),
		('vision', 'Life'),
		('other', 'Other'),
	]
	plan_id = models.CharField(max_length=70)
	plan_name = models.CharField(max_length=50)
	type = models.CharField(max_length=50, choices=TYPES)
	group_number = models.CharField(max_length=100)
	
class PatientInsurance(Record):
	coverage_start_date = models.DateField()
	coverage_end_date = models.DateField()
	patient = models.ForeignKey('patient.Patient')
	insurance = models.ForeignKey('Insurance')
	status = models.CharField(max_length=50)
	subscriber_policy_id = models.CharField(max_length=100)
