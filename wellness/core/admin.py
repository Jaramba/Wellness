from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from guardian.admin import GuardedModelAdmin

from forms import *
from models import *

class ModelAdminMedia(GuardedModelAdmin):
	def has_change_permission(self, request, obj=None):
		has_model_permission = super(ModelAdminMedia, self).has_change_permission(request, obj=None)
		return has_model_permission

	def has_delete_permission(self, request, obj=None):
		has_model_permission = super(ModelAdminMedia, self).has_delete_permission(request, obj=None)
		return has_model_permission
	
	def queryset(self, request):
		qs = super(ModelAdminMedia, self).queryset(request)
		
		if request.user.is_superuser:
		    return qs

		return qs.filter(added_by=request.user)
	   
	def save_model(self, request, obj, form, change):
	    """
	    Given a model instance save it to the database.
	    """
	    obj.save()
	
	def save_formset(self, request, form, formset, change):
	    """
	    Given an inline formset save it to the database.
	    """
	    formset.save()
	
	def get_object(self, request, object_id):
		"""
		Returns an instance matching the primary key provided. ``None``  is
		returned if no match is found (or the object_id failed validation
		against the primary key field).
		"""
		queryset = self.queryset(request)
		model = queryset.model
		try:
		    object_id = model._meta.pk.to_python(object_id)
		    return queryset.get(pk=object_id)
		except (model.DoesNotExist, ValidationError):
		    return None

class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    form = UserProfileInlineForm
    extra = 1

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
		
	def approve_healthworker_profiles(self, request, queryset):
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

	def deactivate(self, request, queryset):
		for user in queryset:
			user.is_active = False
			user.save()
	deactivate.description = 'Deactivate User'

	def approve_patient_profiles(self, request, queryset):
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
	approve_patient_profiles.description = 'Approve Patient'			
	
	list_display = ('username', 'email', 'title', first_name, 'middle_name', last_name, 'mobile_phone', 'is_staff')
	search_fields = ('username', 'first_name', 'last_name', 'email')
	inlines = (UserProfileAdmin,)
	
	actions = [deactivate, approve_patient_profiles, approve_healthworker_profiles]

class PersonAdmin(admin.ModelAdmin):
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
    class ItemAdmin(ModelAdminMedia):
        model = M
        list_display = [f.name for f in M._meta.fields]
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(User)
admin.site.register(User, UserUserProfileAdmin)
admin.site.register(RelationshipType)