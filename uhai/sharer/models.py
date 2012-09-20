from django.db import models
from datetime import datetime, timedelta
from django.contrib.contenttypes import generic

from uhai.core.models import OwnerModel, MetaData

class Sharer(OwnerModel):
	content_type = models.ForeignKey('contenttypes.ContentType')
	object_pk = models.CharField(max_length=80)
	
	content_object = generic.GenericForeignKey('content_type','object_pk')
	
	shared_by = models.ForeignKey('auth.User', related_name='shared_by')
	shared_to = models.ForeignKey('auth.User', related_name='shared_to')
	expires   = models.DateTimeField(default=datetime.now() + timedelta(days=5), help_text='By default, The details expires after 5 days')
	
	def __unicode__(self):
		return 'Shared: %s to %s' % (self.content_type, self.shared_to)

class ShareRequest(OwnerModel):
	requestor = models.ForeignKey('auth.User', related_name='requestor')
	requestee = models.ForeignKey('auth.User', related_name='requestee')
	app_label = models.CharField(max_length=30)
	model     = models.CharField(max_length=30)
	
	def __unicode__(self):
		return '%s.%s requested by %s' % (self.requestor,self.app_label,self.model)
