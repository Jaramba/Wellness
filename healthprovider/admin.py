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
    
    list_display = [f.name for f in HealthWorker._meta.fields]
    inlines = []

admin.site.register(HealthWorker, HealthWorkerAdmin)
