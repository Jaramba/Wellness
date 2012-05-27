from django.db import models
from wellness.core.models import Record, MetaData 

class Immunization(Record):
	code = models.CharField(max_length=50)
	vaccine = models.ForeignKey('medication.Medication')
	brand_name = models.CharField(max_length=100)
	lot_number = models.CharField(max_length=100)
	route = models.CharField(max_length=100)
	site = models.CharField(max_length=100)
	follow_up_date = models.DateTimeField()
	expiry_date = models.DateTimeField()
	practice_date = models.DateTimeField()

class ProblemType(MetaData):pass
class Problem(models.Model):
	name = models.CharField(max_length=30)	
	code = models.CharField(max_length=50, null=True, blank=True)
	type = models.ForeignKey('ProblemType')
	notes = models.TextField()
	
	def __unicode__(self):
		return '%s' % (self.name)


class TrackingField(models.Model):
	'''
	Every problem is trackable, and has things that are tracked
	That's only its conditional, or is Patient defined,
	or if in a Program
	'''
	name =  models.CharField(max_length=120)
	problem = models.ForeignKey('Problem')
	unit = models.CharField(max_length=50)
	daily_cummulative = models.BooleanField(default=False, help_text="Check here if this is a 'daily cumulative' tracking item (calories, for instance) ")

	upper_normal = models.CharField(max_length=5)
	normal = models.CharField(max_length=5)
	lower_normal = models.CharField(max_length=5)

	upper_severe = models.CharField(max_length=5)
	severe = models.CharField(max_length=5)	
	lower_severe = models.CharField(max_length=5)

	upper_moderate = models.CharField(max_length=5)	
	moderate = models.CharField(max_length=5)
	lower_moderate = models.CharField(max_length=5)

	def __unicode__(self):
		return '%s in %s' % (self.name, self.unit)

class EncounterType(MetaData):pass
class Encounter(models.Model):
	patient = models.ForeignKey("patient.Patient")
	provider = models.ForeignKey('healthprovider.HealthWorker')	
	type = models.ForeignKey('EncounterType')
	patient_complience = models.BooleanField(default=False)
	location = models.CharField(max_length=100)
	encounter_date = models.DateTimeField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	observation_notes = models.TextField()
	
	def __unicode__(self):
		return 'Visit by %s' % (self.patient)

class Order(models.Model):
	encounter = models.ForeignKey('Encounter')
	concept_notes = models.CharField(max_length=500)
	instructions = models.CharField(max_length=500)
	discontinued = models.BooleanField(default=False)
	discontinued_date = models.DateTimeField(editable=False)
	discontinued_by = models.ForeignKey('healthprovider.HealthWorker', editable=False)
	discontinued_reason = models.CharField(max_length=500)

	class Meta:
		verbose_name = "Doctor's Order"
		verbose_name_plural = "Doctors' Orders"
		
class Diagnosis(models.Model):
	problem = models.ForeignKey('Problem')
	approved = models.BooleanField(default=False)
	encounter = models.ForeignKey('Encounter')
	notes = models.TextField()
	
	class Meta:
		verbose_name_plural = 'Diagnoses'

class Test(MetaData):
	expected_outcomes = models.TextField()
	date_added = models.DateTimeField(auto_now=True)

class ProblemTest(Test):
	problem = models.ForeignKey('Problem')

class EncounterTest(models.Model):
	name = models.CharField(max_length=30)
	encounter = models.ForeignKey('Encounter')
	test = models.ForeignKey('Test')
	notes = models.TextField(null=True, blank=True)
	date_administered = models.DateTimeField()
	
class EncounterTestResult(models.Model):
	name = models.CharField(max_length=30)
	encounter_test = models.ForeignKey(EncounterTest)
	inference = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	date_added = models.DateTimeField(auto_now=True)
