from django.db import models
from records.models import Record

class Company(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField()
	location = models.CharField(max_length=200)
	date_edited = models.DateTimeField(auto_now=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		abstract = True
		
	def __unicode__(self):
		return self.name

class HealthInsuranceProvider(Company):pass

class EmployerCompany(Company):
	insurance_providers = models.ManyToManyField('HealthInsuranceProvider')
	
	class Meta:
		verbose_name_plural = 'Employer companies'

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
	STATUS = (
		(0, "Inactive"),
		(1, "Approved"),
		(2, "Suspended"),
		(3, "Expired")
	)
	coverage_start_date = models.DateField()
	coverage_end_date = models.DateField()
	insurance = models.ForeignKey('Insurance', help_text='Type of cover')
	status = models.CharField(max_length=50, choices=STATUS)
	subscriber_policy_id = models.CharField(max_length=100)
