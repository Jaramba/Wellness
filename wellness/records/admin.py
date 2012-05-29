from django.contrib import admin
import models
from django.db.models.base import ModelBase

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
	list_display = [f.name for f in models.Problem._meta.fields]
	inlines = [ProblemTestInline]
admin.site.register(models.Problem, ProblemAdmin)

for M in [x
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and 
		not x._meta.abstract and 
		x.__name__ not in [
				'EncounterTest', 'ProblemTest', 
				'Diagnosis', 'Encounter', 'Order'
			]
		)
]:
	class ItemAdmin(admin.ModelAdmin):
		model = M
		list_display = [f.name for f in M._meta.fields]
		inlines = []
		
		if 'slug' in [f.name for f in M._meta.fields]:
			prepopulated_fields = {'slug':('name',),}
		
	try:
		admin.site.register(M, ItemAdmin)
	except admin.sites.AlreadyRegistered:
		pass