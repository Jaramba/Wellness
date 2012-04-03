from django.contrib import admin
from forms import *
from models import *

class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    form = DoctorAdminForm
    
    readonly_fields = ['date_edited', 'date_created']
    
    list_display = [f.name for f in Doctor._meta.fields]
    inlines = []

admin.site.register(Doctor, DoctorAdmin)
