from django.db import models

from uhai.utils.models import OwnerModel, MetaData
from uhai.portal.sites.reminders.models import Event

from datetime import datetime

class ProblemType(MetaData):pass
class Problem(OwnerModel):
	'''
	Anything that a patient can experience, be it Stress, Disease, Condition, that can be noted down
	'''
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
	
class ICD10Chapter(MetaData):
	'''
	check up ICD10: Just some standard for naming Problems... its a long list though.
	So, they are divided into chapters
	'''
	class Meta:		
		verbose_name = 'ICD 10 Chapter'

class ICD10Block(MetaData):
	'''
	This is a block of ICD10 chapters
	'''
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
		return (self.user.full_name)

class Order(OwnerModel):
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

class Diagnosis(OwnerModel):
	'''
	A diagnosis of a problem on a patient encounter 
	by the approval doctor
	'''
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
