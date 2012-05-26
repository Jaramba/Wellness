from django.contrib import admin
import models
from django.db.models.base import ModelBase

for M in [x
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and 
		not x._meta.abstract)
]:
	class ItemAdmin(admin.ModelAdmin):
		model = M
		list_display = [f.name for f in M._meta.fields]
		inlines = []
		
	try:
		admin.site.register(M, ItemAdmin)
	except admin.sites.AlreadyRegistered:
		pass