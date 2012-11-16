from uhai.core.models import OwnerModel, MetaData
from uhai.portal.my.reminders.models import Event

from django.db import models

class Medication(OwnerModel):
    MEDICATION_TYPE=[
        ('otc','Over the counter'),
        ('prescribed','Prescribed'),
        ('prescribed-otc','Prescribed, over the counter')
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
    name = models.CharField(max_length=200)
    medication_type = models.CharField(max_length=50, choices=MEDICATION_TYPE)
    way_taken = models.CharField(max_length=20, choices=WAY_TAKEN)
    
    min_daily_dose = models.CharField(max_length=50)
    max_daily_dose = models.CharField(max_length=50)
    strength = models.CharField(max_length=50)
    strength_unit = models.CharField(max_length=50, choices=STRENGTH_UNIT)
    side_effects = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.name

class Prescription(OwnerModel):
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
        ('every-hour', 'Hourly'),
        ('twice-a-day', 'Twice daily'),
        ('thrice-a-day', 'Thrice daily'),
        ('four-times-a-day', 'Four times daily'),
        ('five-times-a-day', 'Five times daily'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('three-months', 'Three months'),
        ('six-months', 'Six months'),
        ('nine-months', 'Nine months'),
        ('yearly', 'Yearly')
    ]
    user = models.ForeignKey("auth.User")
    provider = models.ForeignKey('providers.HealthWorker', null=True)

    frequency = models.CharField(choices=PERIODS, max_length=50)
    medication = models.ForeignKey('Medication')
    reason = models.CharField(max_length=300)

    priority = models.CharField(max_length=15, choices=[
        ('low', 'Low'),
        ('medium', 'medium'),
        ('high', 'High'),
    ])

    quantity = models.SmallIntegerField()
    unit = models.CharField(max_length=50, choices=UNIT)
    notes = models.CharField(max_length=2000)


    date_prescribed = models.DateTimeField(auto_now_add=True, null=True)
    clear_dose_by = models.DateTimeField(null=True)
    date_dose_cleared = models.DateTimeField(null=True)

    def __unicode__(self):
        return '%s, %s %s taken %s %s prescribed by %s' % (
            self.medication.name, self.quantity, self.unit, 
            self.get_frequency_display(), 
            self.user, self.provider
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
    code = models.CharField(max_length=50, null=True)
    brand_name = models.CharField(max_length=100, null=True)
    duration_of_protection = models.CharField(max_length=3, help_text='duration time, in years', null=True)
    mode_of_delivery = models.CharField(choices=MODE_OF_DELIVERY, max_length=100)
    follow_up_date = models.DateTimeField(null=True)
    expiry_date = models.DateTimeField(null=True)

    notes = models.CharField(max_length=2000, null=True, blank=True)    

    class Meta:
        permissions = ( 
            ('view_immunization', 'View immunization'), 
        )
