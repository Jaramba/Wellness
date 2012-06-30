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
	
	def full_name(self):
		return self.user.full_name
	list_display = ['patient_number',full_name, 'gender','employer','blood_group']
	search_fields = ['patient_number']
	inlines = [PatientInsuranceAdmin, RelationshipInline]

admin.site.register(Patient, PatientAdmin)
admin.site.register(RelationshipType)
