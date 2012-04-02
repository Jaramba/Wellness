from django.contrib import admin
from forms import *
from models import *

#class PatientInline(admin.TabularInline):
#    model = Publication
#    extra = 1

class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    form = DoctorForm
    
    list_display = [f.name for f in Doctor._meta.fields]
    inlines = []

admin.site.register(Doctor, DoctorAdmin)
