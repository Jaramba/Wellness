from django.db import models
from uhai.core.models import OwnerModel, MetaData

class Event(OwnerModel):
    PERIODS = [
        ('every-hour', 'Hourly'),
        ('twice-a-day', 'Twice daily'),
        ('thrice-a-day', 'Thrice daily'),
        ('four-times-a-day', 'Four times daily'),
        ('five-times-a-day', 'Five times daily'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('three-months', 'Three months'),
        ('six-months', 'Six months'),
        ('nine-months', 'Nine months'),
        ('yearly', 'Yearly')
    ]
    user = models.ForeignKey("auth.User")
    provider = models.ForeignKey('providers.HealthWorker', null=True)

    text = models.CharField(max_length=320, null=True, blank=True)
    frequency = models.CharField(choices=PERIODS, max_length=50)
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.text
