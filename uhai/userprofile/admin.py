from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.contrib.sites.admin import SiteAdmin

from uhai.core.models import SiteAdmin as SiteAdministrator

from uhai.core.utils import *
from uhai.patients.models import Patient
from uhai.providers.models import HealthWorker

from uhai.core.admin import BaseStackedInline

from forms import *
from models import *

class UserProfileAdmin(BaseStackedInline):
    model = UserProfile
    extra = 1
    fk_name = 'user'
    
class HealthWorkerAdmin(BaseStackedInline):
    model = HealthWorker
    extra = 0
    fk_name = 'user'
	
class PatientInlineAdmin(BaseStackedInline):
    model = Patient
    extra = 0
    fk_name = 'user'

'''[profile.id, 'PAT-%s-%s' % (datetime.now().strftime('%Y'), get_random_string(4))]'''

class UserUserProfileAdmin(UserAdmin):
	fieldsets = (
	    (None, {'fields': ('username', 'email', 'password')}),
	    (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
	    (('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	#OK, I tried @staticmethod, didnt work, weirdly, this works
	def title(self, user):return user.profile.title.name or ''
	def first_name(self):return self.profile.first_name or ''
	def middle_name(self, user):return user.profile.middle_name or ''
	def last_name(self):return self.profile.last_name or ''
	def mobile_phone(self, user):return user.profile.mobile_phone or ''
	
	def deactivate(self, request, queryset):
		for user in queryset:
			user.is_active = False
			user.save()
	deactivate.description = 'Deactivate User'

	list_display = ('username', 'email', 'title', first_name, 'middle_name', last_name, 'mobile_phone', 'is_superuser', 'is_staff')
	search_fields = ('username', 'first_name', 'last_name', 'email')
	inlines = [UserProfileAdmin, PatientInlineAdmin, HealthWorkerAdmin]
	form = UserChangeForm
	
	actions = [deactivate]

class SiteAdministratorInline(admin.TabularInline):
    model = SiteAdministrator
    extra = 1
    
class SiteAdminAdmin(SiteAdmin):	
	inlines = [SiteAdministratorInline]
    
admin.site.unregister(User)
admin.site.unregister(Site)

admin.site.register(Site, SiteAdminAdmin)
admin.site.register(User, UserUserProfileAdmin)