from django.contrib import admin

from forms import *
from models import *

from uhai.core.admin import BaseModelAdmin, BaseTabularInline

class EmployerCompanyAdmin(BaseModelAdmin):
    model = EmployerCompany
    list_display = [f.name for f in EmployerCompany._meta.fields]
    inlines = []
admin.site.register(EmployerCompany, EmployerCompanyAdmin)

class InsuranceTabularAdmin(BaseTabularInline):
    model = Insurance
    extra = 0

class HealthInsuranceProviderAdmin(BaseModelAdmin):
    model = HealthInsuranceProvider
    list_display = [f.name for f in HealthInsuranceProvider._meta.fields]
    inlines = [InsuranceTabularAdmin]
admin.site.register(HealthInsuranceProvider, HealthInsuranceProviderAdmin)

class InsuranceTypeAdmin(BaseModelAdmin):
    model = InsuranceType
admin.site.register(InsuranceType, InsuranceTypeAdmin)
