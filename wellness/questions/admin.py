from django.contrib import admin
import models
from django.db.models.base import ModelBase

class QuestionInline(admin.TabularInline):
	model = models.Question
	extra = 1

class QuestionSetAdmin(admin.ModelAdmin):
	model = models.QuestionSet
	list_display = [f.name for f in models.QuestionSet._meta.fields]
	inlines = [QuestionInline]

admin.site.register(models.QuestionSet, QuestionSetAdmin)

for M in [x 
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and 
		not x._meta.abstract and 
		x.__name__ not in ['QuestionSet', 'Question'])
]:
    class ItemAdmin(admin.ModelAdmin):
        model = M
        list_display = [f.name for f in M._meta.fields]
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass
