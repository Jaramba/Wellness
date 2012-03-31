from models import *
from forms import *
from django.contrib import admin

#class PatientInline(admin.TabularInline):
#    model = Publication
#    extra = 1

class DoctorAdmin(admin.ModelAdmin):
    model = CV
    form = DoctorForm
    
    list_display = [f.name for f in Doctor._meta.fields]
    inlines = []

admin.site.register(Doctor, DoctorAdmin)
