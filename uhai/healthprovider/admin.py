from django.contrib import admin
from forms import *
from models import *

class HealthCareFacilityAdmin(admin.ModelAdmin):
    model = HealthCareFacility
    
    list_display = [f.name for f in HealthCareFacility._meta.fields]
    inlines = []
admin.site.register(HealthCareFacility, HealthCareFacilityAdmin)
    
class HealthWorkerAdmin(admin.ModelAdmin):
    model = HealthWorker
    list_display = ['title','first_name','middle_name','last_name','mobile_phone','country']

admin.site.register(HealthWorker, HealthWorkerAdmin)

class SpecialityAdmin(admin.ModelAdmin):
	model = Speciality

	list_display = [f.name for f in Speciality._meta.fields]
	prepopulated_fields = {'slug':('name',),}

admin.site.register(Speciality, SpecialityAdmin)

class SpecialityCategoryAdmin(admin.ModelAdmin):
    model = SpecialityCategory
    
    list_display = [f.name for f in SpecialityCategory._meta.fields]

admin.site.register(SpecialityCategory, SpecialityCategoryAdmin)