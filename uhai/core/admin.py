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

for M in [Country, County, Province]:
    class ItemAdmin(ModelAdminMedia):
        model = M
        list_display = [f.name for f in M._meta.fields]
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass
		
admin.site.register(RelationshipType)