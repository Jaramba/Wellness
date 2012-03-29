# coding=UTF-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userprofile.countries import CountryField, COUNTRIES

import datetime
from taggit.managers import TaggableManager
from recruit.models import *
from django.contrib.auth import authenticate

class UserProfile(models.Model):
    """
    User profile model
    """
    GENDER = (('male','Male'),('female','Female'))
    EDUCATION = (
        ('school-of-life','School of life'),
        ('high-school','High School'),
        ('graduate','Graduate'),
        ('post-graduate','Post Graduate'),
        ('phd','PhD'),
        ('professor','Professor')
    )
    
    user = models.ForeignKey(User, unique=True)
    
    #----Applicant---------
    gender = models.CharField(max_length=6, choices=GENDER, null=True, blank=True, help_text="Whats your gender?")
    birthday = models.DateField("Birthday", null=True, blank=True, help_text="When were you born?")
    education = models.CharField(max_length=16, choices=EDUCATION, null=True, blank=True, help_text="What is the highest level of Education you have attained?")
    tags = TaggableManager()
    #----------------------
    
    default_dashboard = models.CharField(
          max_length=15, null=True, blank=True, 
          default="applicant",
          choices=(("applicant","Applicant"),("company","Company"))
    )
    
    #----Recruiter---------
    companies = models.ManyToManyField(Company,
        help_text="""Hold down "Control", or "Command" on a Mac, to select more than one."""
    )
    #----------------------
    
    units = models.IntegerField("Profile units", default=0, editable=False)
    
    city = models.CharField("Current city/town", max_length=120, null=True, blank=True, help_text="What is your home city/town?")
    postal_address = models.CharField("Postal Address", max_length=120, null=True, blank=True, help_text="What is your postal address")
    phone = models.CharField("Phone", max_length=120, help_text="What phone number can you be contacted through?")
    picture = models.CharField("Profile Picture", max_length=400, null=True, blank=True)
    
    country = CountryField("Current Country", help_text="What is your home country?")
    is_active_profile = models.BooleanField(default=False)
    
    description = models.CharField("Bio", max_length=200, null=True, blank=True, help_text="A brief about myself")
    views = models.IntegerField("Views", default=0, blank=True, null=True, editable=False)
    
    last_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return _("%s's profile") % self.user
    
    @property
    def printable_country(self):
        for country in COUNTRIES:
            if country[0] == self.country:
                return country[1]
    @property
    def age(self):
        delta = datetime.now() - self.birthday
        return delta.days/365
        
        
        
        
    @models.permalink
    def get_absolute_url(self):
        return ("public-profile", [self.user.username])
    
    def authenticate(self):
        return authenticate(account=self)

    def get_avatar_url(self):
        return None

    def get_provider(self):
        raise NotImplementedError


    def get_provider_account(self):
        for f in ['twitteraccount', 'openidaccount', 'facebookaccount']:
            try:
                return getattr(self, f)
            except self._meta.get_field_by_name(f)[0].model.DoesNotExist:
                pass
        assert False
User.profile = property(lambda self:UserProfile.objects.get_or_create(user=self)[0])

class RecentActivity(models.Model):
    log = models.CharField(max_length=400)
    user = models.ForeignKey(User)
    time_entered = models.DateTimeField(auto_now_add=True)

class Badge(models.Model):
    name = models.CharField(max_length=6)
    points_required = models.IntegerField()
    date_created = models.DateField("Start date", null=True, blank=True, auto_now_add=True)
    
class UserBadges(models.Model):
    badge = models.ForeignKey(Badge, unique=True)
    applicant = models.ForeignKey(User, unique=True)
    