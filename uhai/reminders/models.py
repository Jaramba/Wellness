from django.db import models
from uhai.core.models import Record, MetaData

class Event(models.Model):
	PERIODS = [
		('every-hour', 'Hourly'),
		('twice-a-day', 'Twice a  day'),
		('thrice-a-day', 'Thrice a day'),
		('four-times-a-day', 'Four times a day'),
		('five-times-a-day', 'Five times a day'),
		('six-times-a-day', 'Six times a day'),
		('seven-times-a-day', 'Seven times a day'),
		('eight-times-a-day', 'Eight times a day'),
		('weekly', 'Weekly'),
		('monthly', 'Monthly'),
		('three-months', 'Three months'),
		('six-months', 'Six months'),
		('nine-months', 'Nine months'),
		('yearly', 'Yearly')
	]
	user    = models.ForeignKey("patients.Patient", verbose_name="Patient")
	provider = models.ForeignKey('providers.HealthWorker', null=True)
	
	text = models.CharField(max_length=50, null=True, blank=True)
	frequency = models.CharField(choices=PERIODS, max_length=50)
	completed = models.BooleanField(default=False)
	start_time = models.DateTimeField()
	end_time   = models.DateTimeField()
	
	def __unicode__(self):
		return self.text
	
	class Meta:pass