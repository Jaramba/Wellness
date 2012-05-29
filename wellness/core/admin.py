from django.contrib import admin
from forms import *
from models import *
from django.contrib.auth.admin import UserAdmin

class ModelAdminMedia(object):
	class Media:
		pass
		
class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    form = UserProfileInlineForm
    extra = 1

def approve_healthworker_profiles(modeladmin, request, queryset):
	for user in queryset:   
		profile = user.profile
		if profile.user.is_healthworker:
			try:
			    profile.healthworker
			    profile.user.is_staff = True
			    profile.user.save()
			except:
			    perform_raw_sql("INSERT INTO healthprovider_healthworker (userprofile_ptr_id) VALUES (%s)", [profile.id])
approve_healthworker_profiles.description = 'Approve Health Worker'

def deactivate(modeladmin, request, queryset):
	for user in queryset:
		user.is_active = False
		user.save()
deactivate.description = 'Deactivate User'

def approve_patient_profiles(modeladmin, request, queryset):
	for user in queryset:   
		profile = user.profile
		try:
		    profile.patient
		except:
		    perform_raw_sql(
		        "INSERT INTO patient_patient (userprofile_ptr_id, patient_number) VALUES (%s, %s)", 
		        [profile.id, 'PAT-%s-%s' % 
		        (datetime.now().strftime('%Y'), get_random_string(4))]
		    )

class UserUserProfileAdmin(UserAdmin, ModelAdminMedia):
	fieldsets = (
	    (None, {'fields': ('username', 'email', 'password')}),
	    (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
	    (('Groups'), {'fields': ('groups',)}),
	    (('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	#OK, I tried @staticmethod, didnt work, weirdly, this works
	def title(self, user):
	    return user.profile.title.name or ''
	def first_name(self):
	    return self.profile.first_name or ''
	def middle_name(self, user):
	    return user.profile.middle_name or ''
	def last_name(self):
	    return self.profile.last_name or ''
	def mobile_phone(self, user):
	    return user.profile.mobile_phone or ''
	
	list_display = ('username', 'email', 'title', first_name, 'middle_name', last_name, 'mobile_phone', 'is_staff')
	search_fields = ('username', 'first_name', 'last_name', 'email')
	inlines = (UserProfileAdmin,)
	
	approve_patient_profiles.description = 'Approve Patient'
	
	actions = [deactivate, approve_patient_profiles, approve_healthworker_profiles]

class PersonAdmin(admin.ModelAdmin, ModelAdminMedia):
    model = Person
    list_display = [f.name for f in Person._meta.fields if f.name not in [
          'photo', 
          'country', 
          'nationality', 
          'id', 
          'date_created', 
          'date_edited'
          ]
    ]
    inlines = []
    
    def queryset(self, request):
        qs = super(PersonAdmin, self).queryset(request)
        return qs.filter(userprofile__isnull=True)
    
admin.site.register(Person, PersonAdmin)

for M in [Country, County, Province, Title]:
    class ItemAdmin(admin.ModelAdmin, ModelAdminMedia):
        model = M
        list_display = [f.name for f in M._meta.fields]
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(User)
admin.site.register(User, UserUserProfileAdmin)
admin.site.register(RelationshipType)
