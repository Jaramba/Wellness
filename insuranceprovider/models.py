from django.db import models
from records.models import Record

class InsuranceProvider(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=100)

class Insurance(Record):
	TYPES = [
		('health', 'Health'),
		('dental', 'Dental'),
		('vision', 'Life'),
		('other', 'Other'),
	]
	coverage_start_date = models.DateField()
	coverage_end_date = models.DateField()
	status = models.CharField(max_length=50)
	type = models.CharField(max_length=50, choices=TYPES)
	insurance_provider = models.ForeignKey(InsuranceProvider)
	plan_name = models.CharField(max_length=50)
	plan_id = models.CharField(max_length=70)
	group_number = models.CharField(max_length=100)
	name_of_card = models.CharField(max_length=100)
	subscriber_policy_id = models.CharField(max_length=100)
	
	