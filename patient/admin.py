from django.contrib import admin
from forms import *
from models import *

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = [f.name for f in Patient._meta.fields if f.name not in [
            'smoking', 
            'smoker_type', 
            'duration_smoking',
            'drinking',
            'drinker_type',
            'duration_drinking',
            'excercising_times',
            'excercise_frequency',
            'diet',
            'family_cancer_status',
            'cancer_type',
            'other_diseases',
            'disabilities'
        ]
    ]
    inlines = []

admin.site.register(Patient, PatientAdmin)

class EmergencyContactAdmin(admin.ModelAdmin):
    model = EmergencyContact
    list_display = [f.name for f in EmergencyContact._meta.fields]

admin.site.register(EmergencyContact, EmergencyContactAdmin)    

class KinAdmin(admin.ModelAdmin):
    model = Kin
    list_display = [f.name for f in Kin._meta.fields]

admin.site.register(Kin, KinAdmin)
