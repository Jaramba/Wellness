from django.contrib import admin

from forms import *
from models import *

from uhai.utils.admin import BaseModelAdmin, BaseTabularInline

class EmployerCompanyAdmin(BaseModelAdmin):
    model = EmployerCompany
    list_display = [f.name for f in EmployerCompany._meta.fields
        if f.name not in
        ('model_owner', 'site', 'access_control_list')
    ]
    inlines = []
admin.site.register(EmployerCompany, EmployerCompanyAdmin)

class InsuranceAdmin(BaseModelAdmin):
    list_display = [f.name for f in Insurance._meta.fields 
        if f.name not in
        ('model_owner', 'site', 'access_control_list')
    ]
    inlines = []
    readonly_fields = ['policy_provider']
admin.site.register(Insurance, InsuranceAdmin)
    
class InsuranceTypeAdmin(BaseModelAdmin):
    model = InsuranceType
admin.site.register(InsuranceType, InsuranceTypeAdmin)
