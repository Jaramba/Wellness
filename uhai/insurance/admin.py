from django.contrib import admin

from forms import *
from models import *


class EmployerCompanyAdmin(admin.ModelAdmin):
    model = EmployerCompany
    list_display = [f.name for f in EmployerCompany._meta.fields]
    inlines = []
admin.site.register(EmployerCompany, EmployerCompanyAdmin)

class InsuranceTabularAdmin(admin.TabularInline):
    model = Insurance
    extra = 0

class HealthInsuranceProviderAdmin(admin.ModelAdmin):
    model = HealthInsuranceProvider
    list_display = [f.name for f in HealthInsuranceProvider._meta.fields]
    inlines = [InsuranceTabularAdmin]
admin.site.register(HealthInsuranceProvider, HealthInsuranceProviderAdmin)

class InsuranceTypeAdmin(admin.ModelAdmin):
    model = InsuranceType
admin.site.register(InsuranceType, InsuranceTypeAdmin)
