from django.contrib import admin
from models import *

class TrackingFieldAdmin(admin.ModelAdmin):
    model = TrackingField
    list_display = [f.name for f in TrackingField._meta.fields]

class TrackingRecordAdmin(admin.ModelAdmin):
    model = TrackingRecord
    
    list_display = [f.name for f in TrackingRecord._meta.fields]

class MedicationAdmin(admin.ModelAdmin):
    model = Medication
    
    list_display = [f.name for f in Medication._meta.fields]
    inlines = []
    
class PrescriptionAdmin(admin.ModelAdmin):
    model = Prescription
    
    list_display = [f.name for f in Prescription._meta.fields]
    inlines = []    

admin.site.register(TrackingField, TrackingFieldAdmin)    
admin.site.register(TrackingRecord, TrackingRecordAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
