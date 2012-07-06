from django.db import models
from uhai.core.models import Record, MetaData 
from uhai.reminders.models import Event

from datetime import datetime

class ProblemType(MetaData):pass
class Problem(models.Model):
	name = models.CharField(max_length=30)	
	type = models.ForeignKey(ProblemType, null=True)
	icd10_code = models.CharField(max_length=10, verbose_name='ICD Code', null=True, blank=True)
	icd10_block = models.ForeignKey('ICD10Block', verbose_name='ICD Block', editable=False, null=True)
	detail = models.CharField(max_length=150, null=True, blank=True)
	cause  = models.CharField(max_length=150, null=True, blank=True)
	notes  = models.TextField(null=True)

	def __unicode__(self):
		message = '%s due to %s' % (self.name, self.cause) if self.cause else self.name
		message = '%s: %s' % (message, self.detail) if self.detail else message
		return message
	
	class Meta:
	    permissions = (
	        ('view_problem', 'View problem'), 
	    )

class ICD10Chapter(MetaData):
	class Meta:		
		verbose_name = 'ICD 10 Chapter'

class ICD10Block(MetaData):
	min_code = models.CharField(max_length=10)
	max_code = models.CharField(max_length=10)
	chapter = models.ForeignKey(ICD10Chapter)
	
	class Meta:
		verbose_name = 'ICD 10 Chapter Block'
		permissions = (
			('view_icd10block', 'View icd10block'), 
		)

class EncounterType(MetaData):pass
class Encounter(Event):	
	type = models.ForeignKey('EncounterType')
	patient_complience = models.BooleanField(default=False)
	location = models.CharField(max_length=50, null=True)	
	observation_notes = models.TextField()
	
	def __unicode__(self):
		return (self.user.user.full_name)

class Order(models.Model):
	encounter = models.ForeignKey('Encounter')
	concept_notes = models.CharField(max_length=500)
	instructions = models.CharField(max_length=500)
	discontinued = models.BooleanField(default=False)
	discontinued_date = models.DateTimeField(editable=False)
	discontinued_by = models.ForeignKey('providers.HealthWorker', editable=False)
	discontinued_reason = models.CharField(max_length=500)

	class Meta:
		verbose_name = "Doctor's Order"
		verbose_name_plural = "Doctors' Orders"
		permissions = (
			('view_order', 'View order'), 
		)

class Diagnosis(models.Model):
	problem = models.ForeignKey('Problem')
	approved = models.BooleanField(default=False)
	encounter = models.ForeignKey('Encounter')
	notes = models.TextField()
	
	class Meta:
		verbose_name_plural = 'Diagnoses'
		permissions = (
			('view_diagnosis', 'View diagnosis'), 
		)

	def __unicode__(self):
		return self.problem.name

class TrackingRecord(MetaData):
	diagnosis = models.ForeignKey('Problem', verbose_name="Problem")
			
class TrackingField(MetaData):
	'''
	Every problem is trackable, and has things that are tracked
	That's only its conditional, or is Patient defined,
	or if in a Program
	'''
	PERIODS = [
		('every-hour', 'Hourly'),
		('twice-a-day', 'Twice daily'),
		('thrice-a-day', 'Thrice daily'),
		('four-times-a-day', 'Four times daily'),
		('five-times-a-day', 'Five times daily'),
		('six-times-a-day', 'Six times daily'),
		('seven-times-a-day', 'Seven times daily'),
		('eight-times-a-day', 'Eight times daily'),
		('daily', 'Daily'),
		('weekly', 'Weekly'),
		('monthly', 'Monthly'),
		('three-months', 'Three months'),
		('six-months', 'Six months'),
		('nine-months', 'Nine months'),
		('yearly', 'Yearly')
	]
	tracking_record = models.ForeignKey('TrackingRecord', null=True)
	unit = models.CharField(max_length=25)
	frequency = models.CharField(choices=PERIODS, max_length=50, null=True)
	
	upper_normal = models.CharField(max_length=5)
	normal = models.CharField(max_length=5)
	lower_normal = models.CharField(max_length=5)

	upper_severe = models.CharField(max_length=5)
	severe = models.CharField(max_length=5)
	lower_severe = models.CharField(max_length=5)

	upper_moderate = models.CharField(max_length=5)	
	moderate = models.CharField(max_length=5)
	lower_moderate = models.CharField(max_length=5)
	
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s in %s' % (self.name, self.unit)

class TrackingEntry(models.Model):
	patient = models.ForeignKey('patients.Patient')	
	field = models.ForeignKey(TrackingField)
	value = models.CharField(max_length=5)
	
	date_updated = models.DateTimeField(default=datetime.now)
	
	class Meta:
		verbose_name_plural = 'Tracking entries'
		
	def __unicode__(self):
		return 'Tracking entry for: %s' % self.field
		
class Test(MetaData):
	expected_outcomes = models.TextField()
	date_added = models.DateTimeField(auto_now=True)

class ProblemTest(Test):
	problem = models.ForeignKey('Problem')

class EncounterTest(Event):
	name = models.CharField(max_length=30)
	test = models.ForeignKey('Test')
	notes = models.TextField(null=True, blank=True)
	
class EncounterTestResult(Event):
	name = models.CharField(max_length=30)
	encounter_test = models.ForeignKey(EncounterTest)
	inference = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)

	