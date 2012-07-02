from django.db import models
from uhai.core.models import Record, MetaData
from uhai.reminders.models import Event

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
        return self.name

class Prescription(Event):
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
    medication = models.ForeignKey('Medication')    
    reason = models.CharField(max_length=300)
    
    quantity = models.SmallIntegerField()
    unit = models.CharField(max_length=50, choices=UNIT)
    period = models.CharField(max_length=50, choices=PERIODS)
    notes = models.CharField(max_length=2000)
    
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

class Immunization(Event):
	MODE_OF_DELIVERY = [
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
	code = models.CharField(max_length=50)
	vaccine = models.ForeignKey(Medication)
	brand_name = models.CharField(max_length=100)
	duration_of_protection = models.CharField(max_length=3, help_text='duration time, in years')
	mode_of_delivery = models.CharField(choices=MODE_OF_DELIVERY, max_length=100)
	follow_up_date = models.DateTimeField()
	expiry_date = models.DateTimeField()

	class Meta:
		permissions = ( 
			('view_immunization', 'View immunization'), 
		)
