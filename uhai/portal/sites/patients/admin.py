from django.contrib import admin
from models import *
from uhai.portal.sites.insurance.models import PatientInsurance
from uhai.portal.sites.providers.models import PatientProvider
from uhai.portal.sites.programs.models import EnrolledProgram

from uhai.core.admin import BaseModelAdmin, BaseTabularInline

class PatientInsuranceAdmin(BaseTabularInline):
    model = PatientInsurance
    extra = 0
	
class PatientProviderAdmin(BaseTabularInline):
    model = PatientProvider
    extra = 0

class EnrolledProgramAdmin(BaseTabularInline):
    model = EnrolledProgram
    extra = 0
	
class RelationshipInline(BaseTabularInline):
	model = Relationship
	fk_name = 'person_a'
	extra = 2

class PatientAdmin(BaseModelAdmin):
	model = Patient
	readonly_fields = [f.name for f in Patient._meta.fields if
        f.name not in ('id', 'model_owner', 'site', 'access_control_list')
    ]

	def full_name(self):
		return self.user.full_name

	list_display = [full_name, 'gender','employer','blood_group']
	inlines = [PatientInsuranceAdmin, PatientProviderAdmin, EnrolledProgramAdmin]

admin.site.register(Patient, PatientAdmin)
admin.site.register(RelationshipType)
