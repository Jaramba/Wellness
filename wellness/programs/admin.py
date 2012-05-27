from django.contrib import admin
import models
from django.db.models.base import ModelBase

class ProgramWorkflowStateInline(admin.TabularInline):
	model = models.ProgramWorkflowState
	extra = 1

class ProgramWorkflowAdmin(admin.ModelAdmin):
	model = models.ProgramWorkflow
	list_display = [f.name for f in models.ProgramWorkflow._meta.fields]
	inlines = [ProgramWorkflowStateInline]

admin.site.register(models.ProgramWorkflow, ProgramWorkflowAdmin)

for M in [x
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and
		not x._meta.abstract and 		
		x.__name__ not in [
				'ProgramWorkflowState', 'ProgramWorkflow'
			]
		)
]:
	class ItemAdmin(admin.ModelAdmin):
		model = M
		list_display = [f.name for f in M._meta.fields]
		inlines = []
		
	try:
		admin.site.register(M, ItemAdmin)
	except admin.sites.AlreadyRegistered:
		pass
