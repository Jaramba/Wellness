from django.db import models
from core.models import *
from core.models import Record

class Image(Record):
    date = models.DateField()

class Ailment(Record):
    date_of_diagnosis = models.DateField()
    
    class Meta:
        abstract=True
    
class Allergy(Ailment):
    severity = models.CharField(max_length=30)
    reaction = models.CharField(max_length=30)
    occurence = models.CharField(max_length=30)
    
    class Meta:
        abstract=True
    
class Condition(Ailment):
    status = models.CharField(max_length=50)
    primary_provider = models.CharField(max_length=50)
    secondary_provider = models.CharField(max_length=50)

class Surgery(Record):
    reason = models.CharField(max_length=300)
    facility = models.CharField(max_length=100)
    attending_physician = models.ForeignKey('healthprovider.HealthWorker')
    date = models.DateField()

class Immunisation(Record):
    dose_sequence_no = models.CharField(max_length=20)
    date_administered = models.DateField()
    