from django.db import models, transaction
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from django.db import models
from datetime import datetime

from django.core.exceptions import PermissionDenied

from django_hosts.managers import HostSiteManager
import fields

from utils import has_permissions

class OwnerModel(models.Model):
    site = models.ForeignKey('sites.Site', null=True, editable=False, related_name="%(app_label)s_%(class)s")
    model_owner = models.ForeignKey('auth.User', verbose_name="Model Owner", null=True, editable=False, related_name="%(app_label)s_%(class)s")
    access_control_list = fields.ACLField(null=True, blank=True, editable=False)
        
    objects = HostSiteManager()
           
    class Meta:
        abstract=True
        
    def delete(self, request=None, *args, **kwargs):
        if has_permissions(request, self, 'delete'):
            super(OwnerModel, obj).delete(*args, **kwargs)
        else:
            messages.warning(request, "You do not have the Permission to delete Item #%s" % obj.pk)
    
    def save(self, request=None, *args, **kwargs):
        if not self.pk:#if Does not already have a PK...
            if request:
                self.access_control_list  = isinstance(self.access_control_list, dict) or {}
                    
                if request.user.is_superuser:
                    user = User.objects.get(pk=0)
                    self.model_owner = user
                    self.access_control_list['system'] = {
                        'view'  : True,
                        'delete': False,
                        'edit'  : False
                    }
                else:
                    self.model_owner = request.user
                    self.access_control_list[request.user.username] = (
                        self.access_control_list.get(request.user.username, {})
                    )
                    self.access_control_list[request.user.username] = {
                        'view'  : True,
                        'delete': True,
                        'edit'  : True
                    }
                self.site = Site.objects.get_current()
                
        return super(OwnerModel, self).save(*args, **kwargs)

class Record(OwnerModel):
    name = models.CharField(max_length=30)
    patient = models.ForeignKey("patients.Patient")
    notes = models.TextField()
    
    class Meta:
        abstract=True

class MetaData(OwnerModel):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True, default=datetime.now)
    date_changed = models.DateTimeField(auto_now_add=True, default=datetime.now)
        
    def __unicode__(self):
        return self.name
    
    class Meta:
        abstract=True

class Country(OwnerModel):
    name = models.CharField(max_length=150)
    iso = models.CharField(max_length=4)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'
        
class Province(OwnerModel):
    name = models.CharField(max_length=150)
    iso = models.CharField(max_length=4)
    country = models.ForeignKey(Country)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Provinces'
        
class County(OwnerModel):
    name = models.CharField(max_length=150)
    iso = models.CharField(max_length=4)
    province = models.ForeignKey(Province)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Counties'

class SiteAdmin(models.Model):
    site = models.ForeignKey('sites.Site')
    site_admin = models.ForeignKey('auth.User')
    