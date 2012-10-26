from django.db import models
from datetime import datetime, timedelta
from django.contrib.contenttypes import generic

from uhai.core.models import OwnerModel, MetaData

class EncountersSharer(OwnerModel):	
    encounter = models.ManyToManyField('records.Encounter', through='EncounterRequest')

    approved = models.BooleanField(default=False)

    shared_by = models.ForeignKey('auth.User', related_name='shared_by')
    shared_to = models.ForeignKey('auth.User', related_name='shared_to')
    expires   = models.DateTimeField(default=datetime.now() + timedelta(days=30), help_text='By default, The details expires after 30 days')

    def __unicode__(self):
        return 'Shared: %s encounters to %s' % (self.shared_by, self.shared_to)

class EncounterRequest(OwnerModel):
    patient = models.ForeignKey('records.Encounter')
    provider = models.ForeignKey('EncountersSharer')
    approved = models.BooleanField(default=False)