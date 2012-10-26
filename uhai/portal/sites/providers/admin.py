from django.contrib import admin
from forms import *
from models import *

from uhai.portal.api.core.admin import BaseModelAdmin, BaseTabularInline

class HealthCareFacilityAdmin(BaseModelAdmin):
    model = HealthCareFacility
    
    list_display = [
    	f.name for f in HealthCareFacility._meta.fields if f.name not in
    	('model_owner', 'site', 'access_control_list')
    ]
    inlines = []
admin.site.register(HealthCareFacility, HealthCareFacilityAdmin)
    
class SpecialityAdmin(BaseModelAdmin):
	model = Speciality

	list_display = [
		f.name for f in Speciality._meta.fields if f.name
		not in ('model_owner', 'site', 'access_control_list')
	]
	prepopulated_fields = {'slug':('name',),}

admin.site.register(Speciality, SpecialityAdmin)

class SpecialityCategoryAdmin(BaseModelAdmin):
    model = SpecialityCategory
    
    list_display = [
    	f.name for f in SpecialityCategory._meta.fields if f.name not in 
    	('model_owner', 'site', 'access_control_list')
    ]

admin.site.register(SpecialityCategory, SpecialityCategoryAdmin)

class HealthWorkerAdmin(BaseModelAdmin):
	list_display = [f.name for f in HealthWorker._meta.fields 
		if f.name not in ('model_owner', 'site', 'access_control_list', id)
    ]

	def full_name(self):
		return self.user.full_name

	readonly_fields = [full_name]
    
admin.site.register(HealthWorker, HealthWorkerAdmin)