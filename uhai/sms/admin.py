from models import *
from django.contrib import admin
from django.contrib.sites.models import Site 

class SmsMessageOutboxAdmin(admin.ModelAdmin):
	model = SmsMessageOutbox
	date_hierarchy = 'queued_at'
	list_display = ['destination', 'text', 'queued_at', 'timestamp', 'gateway_response']
           
# admin.site.unregister(Site)
admin.site.register(SmsMessageOutbox, SmsMessageOutboxAdmin)
admin.site.register(SmsMessageInbox)
