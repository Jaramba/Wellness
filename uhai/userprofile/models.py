from django.contrib.auth.models import User, Group
from django.db import models

class Title(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

class Person(models.Model):
	'''
	Not Everyone is a patient; This will act as a staging profile, until someone
	gets an account.... hmmm, should we create an inactive user or just this?
	'''
	title = models.ForeignKey(Title, null=True)
	relationship = models.ManyToManyField(
		'self',
		through='core.Relationship',
		symmetrical=False,
	)

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
	
	latitude = models.CharField(max_length=50, null=True, blank=True, editable=False)
	longitude = models.CharField(max_length=50, null=True, blank=True, editable=False)
	
	date_edited = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.full_name
	
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
		verbose_name = 'Person'
        permissions = (
            ('view_person', 'View person'),
        )

class UserProfile(Person):
	user = models.OneToOneField('auth.User')
	national_id = models.CharField(max_length=25)
	
	def __unicode__(self):
		return self.full_name
	
	class Meta:
		verbose_name = 'System User profile'
        permissions = (
            ('view_userprofile', 'View User profile'),
        )
	
	@property
	def full_name(self):
		return u' '.join([i for i in (
					(self.title.name if self.title else ''),
					self.first_name,
					(self.middle_name if self.middle_name else ''),
					self.last_name
				) if i
			])

#User Hacks... But everybody is a patient
User.is_healthworker = property(lambda self: self.groups.filter(name='Health Worker').count())
User.is_employer = property(lambda self: self.groups.filter(name='Employer').count())
User.is_admin = property(lambda self: self.groups.filter(name='Admin').count())
User.is_insuranceagent = property(lambda self: self.groups.filter(name='Insurance Agent').count())

User.full_name = property(lambda self: self.profile.full_name)
User.get_full_name = lambda self: self.full_name
User.__unicode__ = lambda self: self.full_name if self.full_name.split(' ') else self.username

def get_profile(self):
	if not hasattr(self, '_profile_cache'):
		self._profile_cache = UserProfile.objects.get_or_create(user=self)[0] if self.pk else None
	return self._profile_cache

User.get_profile = get_profile
User.profile = property(get_profile)
