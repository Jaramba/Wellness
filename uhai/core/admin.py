from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from django.core.exceptions import PermissionDenied
from django.contrib.admin import helpers
from django.contrib.admin.util import get_deleted_objects, model_ngettext
from django.db import router
from django.template.response import TemplateResponse
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext, ugettext_lazy as _

from django.forms.models import (inlineformset_factory, BaseInlineFormSet)

import forms
import models

from utils import has_permissions

from uhai.core import forms as core_forms

from django.forms.models import modelform_factory

def delete_selected(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    app_label = opts.app_label

    # Check that the user has delete permission for the actual model
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied

    using = router.db_for_write(modeladmin.model)

    # Populate deletable_objects, a data structure of all related objects that
    # will also be deleted.
    deletable_objects, perms_needed, protected = get_deleted_objects(
        queryset, opts, request.user, modeladmin.admin_site, using)

    # The user has already confirmed the deletion.
    # Do the deletion and return a None to display the change list view again.
    if request.POST.get('post'):
        if perms_needed:
            raise PermissionDenied
        n = queryset.count()
        if n:
            for obj in queryset:
                obj_display = force_unicode(obj)
                modeladmin.log_deletion(request, obj, obj_display)
            for o in queryset:
                o.delete(request=request)
            modeladmin.message_user(request, _("Successfully deleted %(count)d %(items)s.") % {
                "count": n, "items": model_ngettext(modeladmin.opts, n)
            })
        # Return None to display the change list page again.
        return None

    if len(queryset) == 1:
        objects_name = force_unicode(opts.verbose_name)
    else:
        objects_name = force_unicode(opts.verbose_name_plural)

    if perms_needed or protected:
        title = _("Cannot delete %(name)s") % {"name": objects_name}
    else:
        title = _("Are you sure?")

    context = {
        "title": title,
        "objects_name": objects_name,
        "deletable_objects": [deletable_objects],
        'queryset': queryset,
        "perms_lacking": perms_needed,
        "protected": protected,
        "opts": opts,
        "app_label": app_label,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
    }

    # Display the confirmation page
    return TemplateResponse(request, modeladmin.delete_selected_confirmation_template or [
        "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
        "admin/%s/delete_selected_confirmation.html" % app_label,
        "admin/delete_selected_confirmation.html"
    ], context, current_app=modeladmin.admin_site.name)

delete_selected.short_description = _("Delete selected %(verbose_name_plural)s")

class CoreBaseInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):        
        super(CoreBaseInlineFormSet, self).__init__(*args, **kwargs)

    def save_existing(self, form, instance, commit=True, request=None):
        """Saves and returns an existing model instance for the given form."""
        return form.save(commit=commit, request=request)
        
    def save_existing_objects(self, commit=True, request=None):
        self.changed_objects = []
        self.deleted_objects = []
        if not self.initial_forms:
            return []

        saved_instances = []
        for form in self.initial_forms:
            pk_name = self._pk_field.name
            raw_pk_value = form._raw_value(pk_name)

            # clean() for different types of PK fields can sometimes return
            # the model instance, and sometimes the PK. Handle either.
            pk_value = form.fields[pk_name].clean(raw_pk_value)
            pk_value = getattr(pk_value, 'pk', pk_value)

            obj = self._existing_object(pk_value)
            if self.can_delete and self._should_delete_form(form):
                self.deleted_objects.append(obj)
                obj.delete()
                continue
            if form.has_changed():
                self.changed_objects.append((obj, form.changed_data))
                saved_instances.append(self.save_existing(form, obj, commit=commit, request=request))
                if not commit:
                    self.saved_forms.append(form)
        return saved_instances
        
    def save(self, commit=True, request=None):
        if not commit:
            self.saved_forms = []
            def save_m2m():
                for form in self.saved_forms:
                    form.save_m2m()
            self.save_m2m = save_m2m
        return self.save_existing_objects(commit, request=request) +  self.save_new_objects(commit, request=request)
            
    def save_new(self, form, commit=True, request=None):
        # Use commit=False so we can assign the parent key afterwards, then
        # save the object.
        obj = form.save(commit=False)
        pk_value = getattr(self.instance, self.fk.rel.field_name)
        setattr(obj, self.fk.get_attname(), getattr(pk_value, 'pk', pk_value))
        if commit:
            obj.save(request=request)
        # form.save_m2m() can be called via the formset later on if commit=False
        if commit and hasattr(form, 'save_m2m'):
            form.save_m2m()
        return obj
            
    def save_new_objects(self, commit=True, request=None):
        self.new_objects = []
        for form in self.extra_forms:
            if not form.has_changed():
                continue
            # If someone has marked an add form for deletion, don't save the
            # object.
            if self.can_delete and self._should_delete_form(form):
                continue
            self.new_objects.append(
                self.save_new(
                    form, commit=commit, request=request
                )
            )
            if not commit:
                self.saved_forms.append(form)
        return self.new_objects

class BaseModelAdmin(admin.ModelAdmin):
    actions = [delete_selected]
    def save_model(self, request, obj, form, change):
        obj.save(request=request)

    def save_formset(self, request, form, formset, change):
        formset.save(request=request)
        
    def delete_model(self, request, obj):
        obj.delete(request=request)
        
    def has_change_permission(self, request, obj=None):
        return has_permissions(request, obj, 'edit') if obj else \
            super(BaseModelAdmin, self).has_change_permission(request)

    def has_delete_permission(self, request, obj=None):
        return has_permissions(request, obj, 'delete') if obj else \
            super(BaseModelAdmin, self).has_change_permission(request)
    
class BaseTabularInline(admin.TabularInline):
    actions = [delete_selected]
    formset = CoreBaseInlineFormSet
        
    def save_model(self, request, obj, form, change):
        obj.save(request=request)
        
    def has_change_permission(self, request, obj=None):
        return has_permissions(request, obj, 'edit') if obj else \
            super(BaseTabularInline, self).has_change_permission(request)

    def has_delete_permission(self, request, obj=None):
        return has_permissions(request, obj, 'delete') if obj else \
            super(BaseTabularInline, self).has_change_permission(request)
        
class BaseStackedInline(admin.StackedInline):
    actions = [delete_selected]
    formset = CoreBaseInlineFormSet
    
    def save_model(self, request, obj, form, change):
        obj.save(request=request)
        
    def has_change_permission(self, request, obj=None):        
        return has_permissions(request, obj, 'edit') if obj else \
            super(BaseStackedInline, self).has_change_permission(request)

    def has_delete_permission(self, request, obj=None):
        return has_permissions(request, obj, 'delete') if obj else \
            super(BaseStackedInline, self).has_change_permission(request)
    
for M in [models.Country, models.County, models.Province]:
    class ItemAdmin(BaseModelAdmin):
        list_display = [f.name for f in M._meta.fields if f.name not in (
            'model_owner', 'site', 'access_control_list'
        )]
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass
		