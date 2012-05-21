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

class Reminder(models.Model):
    pattern = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    record = models.ManyToManyField('TrackingRecord')

class PatientTrackingRecord(models.Model):
    patient = models.ForeignKey('patient.Patient')
    tracking_record = models.ForeignKey('TrackingRecord')
    
    def __unicode__(self):
        return 'Tracking %s for %s' % (self.tracking_record, self.patient)

class TrackingRecord(models.Model):
    name = models.CharField(max_length=30)
    notes = models.CharField(max_length=2000, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
class TrackingField(models.Model):
    name =  models.CharField(max_length=120)
    record = models.ForeignKey('TrackingRecord')
    unit = models.CharField(max_length=50)
    daily_cummulative = models.BooleanField(default=False, help_text="Check here if this is a 'daily cumulative' tracking item (calories, for instance) ")
    min_value = models.CharField(max_length=5)
    max_value = models.CharField(max_length=5)
    ideal_min_value = models.CharField(max_length=5)
    ideal_max_value = models.CharField(max_length=5)
    
    def __unicode__(self):
        return self.name

class Image(Record):
    date = models.DateField()

class ProblemType(MetaData):pass
class ProblemStatus(MetaData):pass

class Problem(Record):
    code = models.CharField(max_length=50)
    type = models.ForeignKey('ProblemType')
    source = models.ForeignKey('healthprovider.HealthWorker')
    status = models.ForeignKey('ProblemStatus')

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
