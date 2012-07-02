from django.contrib import admin
from models import *
from uhai.insurance.models import PatientInsurance

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
	
	list_display = [full_name, 'gender','employer','blood_group']
	inlines = [PatientInsuranceAdmin]

admin.site.register(Patient, PatientAdmin)
admin.site.register(RelationshipType)
