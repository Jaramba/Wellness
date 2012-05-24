from django.contrib import admin
from forms import *
from models import *

class EmployerCompanyAdmin(admin.ModelAdmin):
    model = EmployerCompany
    list_display = [f.name for f in EmployerCompany._meta.fields]
    inlines = []
admin.site.register(EmployerCompany, EmployerCompanyAdmin)

class HealthInsuranceProviderAdmin(admin.ModelAdmin):
    model = HealthInsuranceProvider
    list_display = [f.name for f in HealthInsuranceProvider._meta.fields]
    inlines = []
admin.site.register(HealthInsuranceProvider, HealthInsuranceProviderAdmin)

class InsuranceAdmin(admin.ModelAdmin):
    model = Insurance
    list_display = [f.name for f in Insurance._meta.fields]
admin.site.register(Insurance, InsuranceAdmin)
