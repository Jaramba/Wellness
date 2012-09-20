from django.contrib import admin
from forms import *
from models import *

from uhai.core.admin import BaseModelAdmin, BaseTabularInline

class HealthCareFacilityAdmin(BaseModelAdmin):
    model = HealthCareFacility
    
    list_display = [f.name for f in HealthCareFacility._meta.fields]
    inlines = []
admin.site.register(HealthCareFacility, HealthCareFacilityAdmin)
    
class SpecialityAdmin(BaseModelAdmin):
	model = Speciality

	list_display = [f.name for f in Speciality._meta.fields]
	prepopulated_fields = {'slug':('name',),}

admin.site.register(Speciality, SpecialityAdmin)

class SpecialityCategoryAdmin(BaseModelAdmin):
    model = SpecialityCategory
    
    list_display = [f.name for f in SpecialityCategory._meta.fields]

admin.site.register(SpecialityCategory, SpecialityCategoryAdmin)