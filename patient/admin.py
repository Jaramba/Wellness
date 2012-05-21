from django.contrib import admin
from forms import *
from models import *

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ['first_name','middle_name','last_name','gender','mobile_phone','country','employer','blood_group']
    inlines = []

admin.site.register(Patient, PatientAdmin)
