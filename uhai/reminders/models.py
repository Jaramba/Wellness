from django.db import models
from uhai.core.models import Record, MetaData

class Event(models.Model):
	PERIODS = [
		('every-hour', 'Every hour'),
		('twice-a-day', 'Twice a  day'),
		('thrice-a-day', 'Thrice a day'),
		('four-times-a-day', 'Four times a day'),
		('five-times-a-day', 'Five times a day'),
		('six-times-a-day', 'Six times a day'),
		('seven-times-a-day', 'Seven times a day'),
		('eight-times-a-day', 'Eight times a day'),
		('weekly', 'Weekly'),
		('monthly', 'Per month'),
		('three-months', 'Three months'),
		('six-months', 'Six months'),
		('nine-months', 'Nine months'),
		('yearly', 'Per year')
	]
	user    = models.ForeignKey("auth.User", verbose_name="Patient")
	title   = models.CharField(max_length=50)
	message = models.CharField(max_length=140)
	frequency = models.CharField(choices=PERIODS, max_length=50)
	completed = models.BooleanField(default=False)
	start_time = models.DateTimeField()
	end_time   = models.DateTimeField()
	
	def __unicode__(self):
		return self.message
	
	class Meta:pass