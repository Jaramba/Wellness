from django.db import models
from uhai.core.models import Record, MetaData

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
    user = models.ForeignKey('auth.User')
    message = models.CharField(max_length=140)
    frequency = models.CharField(choices=PERIODS, max_length=50)
    start_date = models.DateTimeField('Start Time')
    end_date = models.DateTimeField('End Time')
    