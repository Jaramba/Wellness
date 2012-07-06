from django.contrib import admin
import models
from django.db.models.base import ModelBase
from guardian.admin import GuardedModelAdmin

class ProgramWorkflowStateInline(admin.TabularInline):
	model = models.ProgramWorkflowState
	extra = 1

class EnrolledProgramInline(admin.TabularInline):
	model = models.EnrolledProgram
	extra = 1
	
class ProgramAdmin(admin.ModelAdmin):
	model = models.Program
	list_display = [f.name for f in models.Program._meta.fields]
	inlines = [EnrolledProgramInline]
admin.site.register(models.Program, ProgramAdmin)

class ProgramWorkflowAdmin(admin.ModelAdmin):
	model = models.ProgramWorkflow
	list_display = [f.name for f in models.ProgramWorkflow._meta.fields]
	inlines = [ProgramWorkflowStateInline]
admin.site.register(models.ProgramWorkflow, ProgramWorkflowAdmin)

class QuestionInline(admin.TabularInline):
	model = models.Question
	extra = 1

class QuestionSetAdmin(admin.ModelAdmin):
	model = models.QuestionSet
	list_display = [f.name for f in models.QuestionSet._meta.fields]
	inlines = [QuestionInline]
admin.site.register(models.QuestionSet, QuestionSetAdmin)

class PatientProgramQuestionnaireInline(admin.TabularInline):
	model = models.PatientProgramQuestionnaire
	extra = 0

class ProgramQuestionnaireAdmin(admin.ModelAdmin):
	model = models.ProgramQuestionnaire
	list_display = [f.name for f in models.ProgramQuestionnaire._meta.fields]
	inlines = [PatientProgramQuestionnaireInline]
admin.site.register(models.ProgramQuestionnaire, ProgramQuestionnaireAdmin)

for M in [x
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and
		not x._meta.abstract and 		
		x.__name__ not in [
				'ProgramWorkflowState', 'ProgramWorkflow', 'EnrolledProgram',
				'QuestionSet', 'Question','PatientProgramQuestionnaire'
			]
		)
]:
	class ItemAdmin(GuardedModelAdmin):
		model = M
		list_display = [f.name for f in M._meta.fields if not f.name in ('description', 'is_public','concept_notes','expected_outcome_notes')]
		inlines = []
		
	try:
		admin.site.register(M, ItemAdmin)
	except admin.sites.AlreadyRegistered:
		pass
