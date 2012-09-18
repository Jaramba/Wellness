from django.db import models, transaction
from django.contrib.auth.models import User, Group
from django.db import models
from datetime import datetime

class OwnerModel(models.Model):
    #ACL
    site = models.ForeignKey('sites.Site', null=True, editable=False, related_name="%(app_label)s_%(class)s")
    access_control_list = models.CharField(max_length=30, null=True, editable=False)
    
    class Meta:
        abstract=True

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
        pass#sort = ['name']
        
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
        pass#sort = ['name']
            