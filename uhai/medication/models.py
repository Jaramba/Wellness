from django.db import models
from uhai.core.models import Record, MetaData

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
    way_taken = models.CharField(max_length=20, choices=WAY_TAKEN)
    
    strength = models.CharField(max_length=50)
    min_daily_dose = models.CharField(max_length=50)
    max_daily_dose = models.CharField(max_length=50)
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
    encounter = models.ForeignKey("records.Encounter")
    medication = models.ForeignKey('Medication')
    
    reason = models.CharField(max_length=300)
    
    quantity = models.SmallIntegerField()
    frequency = models.CharField(max_length=50, choices=[(u'%s'%n, '%s time%s' % (n, 's' if n > 1 else '')) for n in range(1,13)])
    unit = models.CharField(max_length=50, choices=UNIT)
    period = models.CharField(max_length=50, choices=PERIODS)
    reminder_type = models.ForeignKey('reminders.ReminderType')
    notes = models.CharField(max_length=2000)	
    
    date_started = models.DateField()
    date_ended = models.DateField()
    date_prescribed = models.DateField()
    next_prescription_date = models.DateField()
    
    def __unicode__(self):
    	return '%s, %s %s taken %s %s for %s, prescribed by %s' % (
    		self.medication.name, self.quantity, self.unit, 
    		self.get_frequency_display(), self.get_period_display(), 
    		self.encounter.patient, self.encounter.provider
    	)
        
    class Meta:
        permissions = ( 
            ('view_prescription', 'View prescription'), 
        )
