from django.contrib import admin
from django.db.models.base import ModelBase

import models

class DiagnosisInline(admin.TabularInline):
	model = models.Diagnosis
	extra = 1

class OrderInline(admin.TabularInline):
	model = models.Order
	extra = 1
	
class EncounterTestInline(admin.TabularInline):
	model = models.EncounterTest
	extra = 1
	
class ProblemTestInline(admin.TabularInline):
	model = models.ProblemTest
	extra = 1

class EncounterAdmin(admin.ModelAdmin):
	model = models.Encounter
	list_display = [f.name for f in models.Encounter._meta.fields]
	inlines = [DiagnosisInline, OrderInline, EncounterTestInline]
admin.site.register(models.Encounter, EncounterAdmin)

class ProblemAdmin(admin.ModelAdmin):
	model = models.Problem
	fields = [f.name for f in models.Problem._meta.fields if f.name not in ('id', 'icd10_block')]
	list_display = fields
	search_fields = fields[:len(fields)/2]
	inlines = [ProblemTestInline]
	
admin.site.register(models.Problem, ProblemAdmin)

class ICD10Blockline(admin.TabularInline):
	model = models.ICD10Block
	extra = 1

class ICD10ChapterAdmin(admin.ModelAdmin):
	model = models.ICD10Chapter
	list_display = [f.name for f in models.ICD10Chapter._meta.fields]
	inlines = [ICD10Blockline]
admin.site.register(models.ICD10Chapter, ICD10ChapterAdmin)

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
	class ItemAdmin(admin.ModelAdmin):
		model = M
		list_display = [f.name for f in M._meta.fields]
		inlines = []
		search_fields = M._meta.fields[:5]
		
		if 'slug' in [f.name for f in M._meta.fields]:
			prepopulated_fields = {'slug':('name',),}
		
	try:
		admin.site.register(M, ItemAdmin)
	except admin.sites.AlreadyRegistered:
		pass