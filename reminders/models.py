from django.db import models
from core.models import Record, MetaData

class ReminderType(MetaData):pass
class Reminder(models.Model):
    pattern = models.CharField(max_length=200)
    datetime = models.DateTimeField()