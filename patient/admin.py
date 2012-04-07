from django.contrib import admin
from forms import *
from models import *

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = [f.name for f in Patient._meta.fields]
    inlines = []

admin.site.register(Patient, PatientAdmin)

class EmergencyContactAdmin(admin.ModelAdmin):
    model = EmergencyContact
    list_display = [f.name for f in EmergencyContact._meta.fields]

admin.site.register(EmergencyContact, EmergencyContactAdmin)    

class PatientKinAdmin(admin.ModelAdmin):
    model = PatientKin
    list_display = [f.name for f in PatientKin._meta.fields]

admin.site.register(PatientKin, PatientKinAdmin)
