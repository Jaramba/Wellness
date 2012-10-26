from django.contrib.auth.models import User, Group
from django.db import models

from django.template.defaultfilters import slugify

from uhai.portal.api.core.models import OwnerModel, MetaData

class Title(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
    title = models.ForeignKey(Title, null=True)

    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True, help_text="Family/Sur-name")

    email = models.CharField(max_length=50, null=True)
    mobile_phone = models.CharField(max_length=50, null=True, help_text="For alerts, (+2547xxxxxxxx)")
    home_phone = models.CharField(max_length=50, null=True, blank=True, help_text="Emergency purposes (+2547xxxxxxxx)")
    work_phone = models.CharField(max_length=50, null=True, blank=True, help_text="Emergency purposes (+2547xxxxxxxx)")

    photo = models.FileField(upload_to='photos', null=True, blank=True)

    postal_code = models.CharField(max_length=50, null=True, blank=True)
    village = models.CharField(max_length=50, null=True, blank=True, help_text='Your home village')
    province = models.ForeignKey('core.Province', null=True, help_text='Your home province')
    county = models.ForeignKey('core.County', null=True, help_text='Your home county')
    country = models.ForeignKey('core.Country', null=True, help_text='Your home country')
        
    user = models.ForeignKey('auth.User', unique=True)
    national_id = models.CharField(max_length=25)

    main_role = models.ForeignKey(Group, null=True, blank=True)
        
    date_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.full_name
        
    @property
    def role(self):
        return slugify(request.user.profile.main_role)

    @property
    def full_name(self):
        return u' '.join([i for i in (
                    (self.title.name if self.title else ''),
                    self.first_name if hasattr(self, 'first_name') else '',
                    (self.middle_name if self.middle_name else ''),
                    self.last_name if hasattr(self, 'last_name') else ''
                ) if i
            ])
    class Meta:
        verbose_name = 'System User profile'
        permissions = (
            ('view_userprofile', 'View User profile'),
        )

    @property
    def full_name(self):
        return u' '.join([i for i in (
                    self.first_name,
                    (self.middle_name if self.middle_name else ''),
                    self.last_name
                ) if i
            ])

#User Hacks... But everybody is a potential patient
User.is_healthworker = property(lambda self: self.groups.filter(name='Health Worker').exists())
User.is_employer = property(lambda self: self.groups.filter(name='Employer').exists())
User.is_insuranceagent = property(lambda self: self.groups.filter(name='Insurance Agent').exists())

User.full_name = property(lambda self: self.profile.full_name if self.profile else None)
User.__unicode__ = (
    lambda (self): 
        self.full_name
        
        if (
            None 
            if not self.full_name
            else
                self.full_name.split(' ')
        )        
        else 
            self.username
)

def get_profile(self):
	if not hasattr(self, '_profile_cache'):
		self._profile_cache = UserProfile.objects.get_or_create(user=self)[0] if self.pk else None
	return self._profile_cache

User.get_profile = get_profile
User.profile = property(get_profile)