from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from uhai.core.utils import *
from uhai.patients.models import Patient
from uhai.providers.models import HealthWorker

from forms import *
from models import *

class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    extra = 1

class HealthWorkerAdmin(admin.StackedInline):
    model = HealthWorker
    extra = 0
	
class PatientInlineAdmin(admin.StackedInline):
	model = Patient
	extra = 0

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
   
admin.site.unregister(User)
admin.site.register(User, UserUserProfileAdmin)