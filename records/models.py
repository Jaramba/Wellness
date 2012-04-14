from django.db import models
from core.models import Record, MetaData 

class Immunization(Record):
    code = models.CharField(max_length=50)
    vaccine = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    expiry_date = models.DateTimeField()
    practice_date = models.DateTimeField(auto_now=True)

class TrackingRecord(models.Model):
    name = models.CharField(max_length=50)
    fields = models.ManyToManyField('TrackingField')
    reminders = models.ManyToManyField('core.Reminder')

class TrackingField(models.Model):
    name = models.CharField(max_length=50)
    patient = models.ForeignKey("patient.Patient")
    unit = models.CharField(max_length=50)
    daily_cummulative = models.BooleanField(default=False)
    min_value = models.CharField(max_length=5)
    max_value = models.CharField(max_length=5)
    ideal_min_value = models.CharField(max_length=5)
    ideal_max_value = models.CharField(max_length=5)

class PatientProgram(models.Model):
    patient = models.ForeignKey("patient.Patient")
    program = models.ForeignKey("Program")
    date_enrolled = models.DateField(auto_now=True)
    date_completed = models.DateField()
    outcome_notes = models.CharField(max_length=2000)
    
class Program(models.Model):
    concept_details = models.CharField(max_length=300)
    outcome_details = models.CharField(max_length=300)
    
class PatientStates(models.Model):
    patient_program = models.ForeignKey("PatientProgram")
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()

class Image(Record):
    date = models.DateField()

class ProblemType(MetaData):pass
class Problem(Record):
    STATUS = ()
    code = models.CharField(max_length=50)
    type = models.ForeignKey('ProblemType')
    details = models.CharField(max_length=150)
    source = models.ForeignKey('healthprovider.HealthWorker')
    status = models.CharField(max_length=16, choices=STATUS)
    
class VisitType(MetaData):pass
class Visit(models.Model):
    patient = models.ForeignKey("patient.Patient")
    indication_notes = models.CharField(max_length=1000)
    type = models.ForeignKey('VisitType')
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now=True)
    stop_time = models.DateTimeField(auto_now=True)

class OrderType(MetaData):pass
class Order(models.Model):
    encounter = models.ForeignKey('Encounter')
    type = models.ForeignKey('OrderType')
    concept_notes = models.CharField(max_length=500)
    instructions = models.CharField(max_length=500)
    discontinued = models.BooleanField(default=False)
    discontinued_date = models.DateTimeField()
    discontinued_by = models.ForeignKey('healthprovider.HealthWorker')
    discontinued_reason = models.CharField(max_length=500)

class EncounterType(MetaData):pass
class Encounter(models.Model):
    patient = models.ForeignKey("patient.Patient")
    observation_notes = models.CharField(max_length=600)
    encounter_provider = models.ForeignKey('healthprovider.HealthWorker')
    encounter_date = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('EncounterType')
    visit = models.ForeignKey('Visit')
    