from django.contrib import admin
import models
from django.db.models.base import ModelBase

class TrackingFieldInlineAdmin(admin.TabularInline):
	model = models.TrackingField
	extra = 1

class TrackingRecordAdmin(admin.ModelAdmin):
	model = models.TrackingRecord
	list_display = [f.name for f in models.TrackingRecord._meta.fields]
	inlines = [TrackingFieldInlineAdmin]

admin.site.register(models.TrackingRecord, TrackingRecordAdmin)
	
for M in [x 
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and 
		not x._meta.abstract and 
		not x.__name__ in ['TrackingRecord', 'TrackingField'])
]:
	class ItemAdmin(admin.ModelAdmin):
		model = M
		list_display = [f.name for f in M._meta.fields]
		inlines = []
		
	try:
		admin.site.register(M, ItemAdmin)
	except admin.sites.AlreadyRegistered:
		pass