from django.db import models

class SmsMessage(models.Model):        
	text = models.CharField(max_length=480)
	queued_at = models.DateTimeField(auto_now_add=True)      

	class Meta:
		abstract = True
	
class SmsMessageInbox(SmsMessage):
	origin = models.CharField(max_length=48)
	timestamp = models.DateTimeField(auto_now=True)

class SmsMessageOutbox(SmsMessage):
	destination = models.CharField(max_length=48)
	gateway_response = models.CharField(max_length=255, null=True, blank=True)
	timestamp = models.DateTimeField(null=True, blank=True)
	