from django.contrib import admin
from models import *

class TrackingItemAdmin(admin.ModelAdmin):
    model = TrackingItem
    
    list_display = [f.name for f in TrackingItem._meta.fields]
    inlines = []
    
class MedicationAdmin(admin.ModelAdmin):
    model = Medication
    
    list_display = [f.name for f in Medication._meta.fields]
    inlines = []
    
class PrescriptionAdmin(admin.ModelAdmin):
    model = Prescription
    
    list_display = [f.name for f in Prescription._meta.fields]
    inlines = []    
    
admin.site.register(TrackingItem, TrackingItemAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
