from django.contrib import admin
from models import *
from uhai.insuranceprovider.models import PatientInsurance

class PatientInsuranceAdmin(admin.TabularInline):
    model = PatientInsurance
    extra = 1

class RelationshipInline(admin.TabularInline):
	model = Relationship
	fk_name = 'person_a'
	extra = 1
	
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['first_name','middle_name','last_name','gender','mobile_phone','country','employer','blood_group']
    inlines = [PatientInsuranceAdmin, RelationshipInline]
	
admin.site.register(Patient, PatientAdmin)
admin.site.register(RelationshipType)