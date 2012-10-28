from django.contrib import admin
from django.db.models.base import ModelBase

from django.forms.models import modelform_factory
from uhai.utils.admin import BaseModelAdmin, BaseTabularInline

import models
import forms 

class DiagnosisInline(BaseTabularInline):
    model = models.Diagnosis
    extra = 0

class OrderInline(BaseTabularInline):
	model = models.Order
	extra = 0
	
class EncounterTestInline(BaseTabularInline):
	model = models.EncounterTest
	extra = 0
	
class ProblemTestInline(BaseTabularInline):
	model = models.ProblemTest
	extra = 0

class EncounterAdmin(BaseModelAdmin):
	model = models.Encounter
	list_display = [f.name for f in models.Encounter._meta.fields if not f.name in (
        'id', 'event_ptr', 'observation_notes', 'message', 'completed', 'location',
        'model_owner', 'site', 'access_control_list'
    )]
	inlines = [DiagnosisInline, OrderInline, EncounterTestInline]
admin.site.register(models.Encounter, EncounterAdmin)

class ProblemAdmin(BaseModelAdmin):
    model = models.Problem
    fields = [f.name for f in models.Problem._meta.fields if f.name not in (
        'id', 'icd10_block', 'model_owner', 'site', 'access_control_list'
    )]
    list_display = fields
    search_fields = fields[:len(fields)/2]
    inlines = [ProblemTestInline]
    readonly_fields = ("site", "model_owner", "access_control_list")
	
admin.site.register(models.Problem, ProblemAdmin)

class ICD10Blockline(BaseTabularInline):
	model = models.ICD10Block
	extra = 1

class ICD10ChapterAdmin(BaseModelAdmin):
	model = models.ICD10Chapter
	list_display = [f.name for f in models.ICD10Chapter._meta.fields]
	inlines = [ICD10Blockline]
admin.site.register(models.ICD10Chapter, ICD10ChapterAdmin)

class ProblemInline(BaseTabularInline):
	model = models.Problem
	extra = 1

class ICD10BlockAdmin(BaseModelAdmin):
    model = models.ICD10Block
    list_display = [f.name for f in models.ICD10Block._meta.fields]
    inlines = [ProblemInline]
admin.site.register(models.ICD10Block, ICD10BlockAdmin)

for M in [x
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and 
		not x._meta.abstract and 
		x.__name__ not in [
				'EncounterTest', 'ProblemTest', 
				'Diagnosis', 'Encounter', 'Order'
				'ICD10Chapter','ICD10Block'
			]
		)
]:
    class ItemAdmin(BaseModelAdmin):
        model = M
        #form = forms.__dict__.get(M.__name__ + 'Formz', 
        #        modelform_factory(M, form=forms.BaseModelForm)
        #)

        list_display = [f.name for f in M._meta.fields if not f.name in (
            'id', 'event_ptr', 'observation_notes', 'message', 'completed', 'location',
            'model_owner', 'site', 'access_control_list'
        )]        
        inlines = []
        search_fields = M._meta.fields[:5]

        if 'slug' in [f.name for f in M._meta.fields]:
            prepopulated_fields = {'slug':('name',),}
        
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass