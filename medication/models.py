from django.db import models
from core.models import Record

class Problem(Record):
    STATUS = ()
    code = models.CharField(max_length=50)
    details = models.CharField(max_length=150)
    status = models.CharField(max_length=16, choices=STATUS)

class Immunization(Record):
    code = models.CharField(max_length=50)
    vaccine = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(auto_now=True)
    practice_date = models.DateTimeField(auto_now=True)

class Diagnosis(Problem):pass
class LabResult(Problem):pass
class Symptom(Problem):
    TYPE = (
        ('chronic', 'Chronic'),
        ('relapsing', 'Relapsing'),
        ('remitting', 'Remitting')
    )
    type = models.CharField(max_length=16, choices=TYPE)
    
class Condition(Problem):pass
    
class Disease(Condition):
    TYPE = (
        ('pathogenic',      'Pathogenic'),
        ('deficiency',      'Deficiency'),
        ('hereditary',      'Hereditary'),
        ('physiological',   'Physiological'),
        ('communicable',   'Communicable'),
        ('non-communicable',   'Non-communicable')
    )
    type = models.CharField(max_length=16, choices=TYPE)

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

class Medication(models.Model):
    MEDICATION_TYPE=[
        ('otc','OTC'),
        ('prescribed','Prescribed'),
        ('prescribed-otc','PrescribedOTC')
    ]
    WAY_TAKEN = [
        ('by-mouth', 'By mouth'),
        ('in-right-ear', 'In Right ear'),
        ('in-both-ears', 'In Both ears'),
        ('in-left-ear', 'In Left ear'),
        ('in-right-eye', 'In Right eye'),
        ('in-both-eyes', 'In Both eyes'),
        ('in-left-eye', 'In Left eye'),
        ('in-nose', 'In Nose'),
        ('inhalation', 'Inhalation'),
        ('intravenous', 'Intravenous'),
        ('topical', 'Topical'),
        ('rectal', 'Rectal'),
        ('vaginal', 'Vaginal'),
        ('under-tongue', 'Under tongue'),
        ('subcataneous', 'Subcataneous'),
    ]
    STRENGTH_UNIT = [
        ('gram', 'Gram (g)'),
        ('milligram', 'Milligram (mg)'),
        ('microgram', 'Microgram (mcg)'),
        ('percent', 'Percent (%)'),
    ]
    
    name = models.CharField(max_length=50)
    medication_type = models.CharField(max_length=10, choices=MEDICATION_TYPE)
    way_taken = models.CharField(max_length=10, choices=WAY_TAKEN)
    
    strength = models.CharField(max_length=50)
    strength_unit = models.CharField(max_length=50, choices=STRENGTH_UNIT)
    side_effects = models.CharField(max_length=200)
    
    def __unicode__(self):
        return '%s type: %s' % (self.name, self.get_medication_type_display()) 

class Prescription(models.Model):
    UNIT = [
        ('tablet', 'Tablet(s)'),         
        ('capsule', 'Capsule(s)'),
        ('lozenge', 'Lozenge(s)'),
        ('drop', 'Drop(s)'),
        ('suppository', 'Suppository'),
        ('ointment', 'Ointment'),
        ('millilitre', 'Millilitre (mL)'),
        ('teaspoon', 'Teaspoon (Tbsp)'),
        ('ounce', 'Ounce (oz)'),
    ]
    PERIODS = [
        ('as-needed', 'As needed'),
        ('per-hour', 'Per hour'),
        ('per-day', 'Per day'),
        ('per-week', 'Per week'),
        ('per-month', 'Per month'),
        ('per-year', 'Per year')
    ]
    patient = models.ForeignKey("patient.Patient")
    medication = models.ForeignKey('Medication')
    
    reason = models.CharField(max_length=300)
    quantity = models.SmallIntegerField()
    frequency = models.CharField(max_length=50, choices=[(u'%s'%n, '%s time%s' % (n, 's' if n > 1 else '')) for n in range(1,13)])
    unit = models.CharField(max_length=50, choices=UNIT)
    period = models.CharField(max_length=50, choices=PERIODS)
    
    prescribed_by = models.ForeignKey('healthprovider.HealthWorker')
    
    notes = models.CharField(max_length=2000)
    
    date_started = models.DateField()
    date_ended = models.DateField()
    
    date_prescribed = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return '%s, %s %s taken %s %s for %s, prescribed by %s' % (
            self.medication.name, self.quantity, self.unit, self.get_frequency_display(), self.get_period_display(), self.patient, self.prescribed_by
        )
