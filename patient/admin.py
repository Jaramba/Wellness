from django.contrib import admin
from models import *
from insuranceprovider.models import PatientInsurance

class PatientInsuranceAdmin(admin.TabularInline):
    model = PatientInsurance
    extra = 1

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['first_name','middle_name','last_name','gender','mobile_phone','country','employer','blood_group']
    inlines = [PatientInsuranceAdmin]

admin.site.register(Patient, PatientAdmin)
