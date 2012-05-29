from django.db import models
from wellness.core.models import Record, MetaData

class ReminderType(MetaData):pass
class Reminder(models.Model):
    PERIODS = [
        ('every-hour', 'Every hour'),
        ('twice-a-day', 'Twice a  day'),
        ('thrice-a-day', 'Thrice a day'),
        ('weekly', 'Weekly'),
        ('monthly', 'Per month'),
        ('three-months', 'Three months'),
        ('six-months', 'Six months'),
        ('nine-months', 'Nine months'),
        ('yearly', 'Per year')
    ]
    patient  = models.ForeignKey('patient.Patient')
    message = models.CharField(max_length=140)
    frequency = models.CharField(choices=PERIODS, max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    