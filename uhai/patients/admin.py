from django.contrib import admin
from models import *
from uhai.insurance.models import PatientInsurance
from uhai.providers.models import PatientProvider
from uhai.programs.models import EnrolledProgram

class PatientInsuranceAdmin(admin.TabularInline):
    model = PatientInsurance
    extra = 0
	
class PatientProviderAdmin(admin.TabularInline):
    model = PatientProvider
    extra = 0

class EnrolledProgramAdmin(admin.TabularInline):
    model = EnrolledProgram
    extra = 0
	
class RelationshipInline(admin.TabularInline):
	model = Relationship
	fk_name = 'person_a'
	extra = 0

class PatientAdmin(admin.ModelAdmin):
	model = Patient
	readonly_fields = [f.name for f in Patient._meta.fields if not f.name == 'id']

	def full_name(self):
		return self.user.full_name

	list_display = [full_name, 'gender','employer','blood_group']
	inlines = [PatientInsuranceAdmin, PatientProviderAdmin, EnrolledProgramAdmin]

admin.site.register(Patient, PatientAdmin)
admin.site.register(RelationshipType)
