from django.db import models, transaction
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from django.db import models
from datetime import datetime

from django.core.exceptions import PermissionDenied

from django_hosts.managers import HostSiteManager
import fields

from funcs import has_permissions

"""
Things to nore: We have the same Database for all the Insurance Companies in the system:
Hence, Multitenancy (http://en.wikipedia.org/wiki/Multitenancy) is the idea here.
So, we will have AON being served at aon.uhai.com, Resolution at resolution.uhai.com
So, all this will be checked at a middleware for the request URL, so that we may parse the
current URL to get the site to redirect to or work with.
"""

class OwnerModel(models.Model):
    """
    For access control purposes, We have a base class that will be extended inorder to 
    have site/person based filtering and data hiding.
    """
    site = models.ForeignKey('sites.Site', null=True, editable=False, related_name="%(app_label)s_%(class)s")
    #The person who created the object or has been given the fll rights to the object
    model_owner = models.ForeignKey('auth.User', verbose_name="Model Owner", null=True, editable=False, related_name="%(app_label)s_%(class)s")
    #A dictionary descrobing who has what rights on this object, if not, just leave it to
    access_control_list = fields.ACLField(null=True, blank=True, editable=False)
        
    #Now lets use a custom Manager that will work with our current site
    objects = HostSiteManager()
           
    class Meta:
        abstract=True
        
    def delete(self, request=None, *args, **kwargs):
        """
        Override delete for the object, making sure that the current user has the permission to delete 
        this object
        """
        if has_permissions(request, self, 'delete'):
            super(OwnerModel, obj).delete(*args, **kwargs)
        else:
            messages.warning(request, "You do not have the Permission to delete Item #%s" % obj.pk)
    
    def save(self, request=None, *args, **kwargs):
        """
        if is not a new object, lets go through the drill: check if user is super user and give right to 
        the system, else just give it to the current user themself
        """
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
    '''
    Base class for patients records
    '''
    name = models.CharField(max_length=30)
    patient = models.ForeignKey("patients.Patient")
    notes = models.TextField()
    
    class Meta:
        abstract=True

class MetaData(OwnerModel):
    '''
    a base class for objects that are simply explainative of other objects
    '''
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
    