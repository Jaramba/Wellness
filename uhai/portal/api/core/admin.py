from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from django.contrib.admin.views.main import ChangeList

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

from utils import has_permissions, delete_selected

from uhai.core import forms as core_forms

from uhai.core.models import OwnerModel
from uhai.core.forms import BaseModelForm

from django.forms.models import modelform_factory

class CoreBaseInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):        
        super(CoreBaseInlineFormSet, self).__init__(*args, **kwargs)

    def save_existing(self, form, instance, commit=True, request=None):
        if issubclass(type(form), BaseModelForm):
            return form.save(commit=commit, request=request)
        else:
            return form.save(commit=commit)
        
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

                if issubclass(type(obj), OwnerModel):
                    saved_instances.append(self.save_existing(form, obj, commit=commit, request=request))                    
                else:
                    saved_instances.append(self.save_existing(form, obj, commit=commit))

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
            
        return (
            self.save_existing_objects(commit, request=request) + 
            self.save_new_objects(commit, request=request)
        )        
            
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

class CoreChangeList(ChangeList):
    def get_query_set(self, request):
        return super(CoreChangeList, self).get_query_set(request)
        
class BaseModelAdmin(admin.ModelAdmin):
    actions = [delete_selected]
    def save_model(self, request, obj, form, change):        
        if issubclass(type(obj), OwnerModel):
            obj.save(request=request)
        else:
            obj.save()      
    
    def save_formset(self, request, form, formset, change):
        formset.save(request=request)
    
    def queryset(self, request):
        queryset = super(BaseModelAdmin, self).queryset(request)
        if issubclass(queryset.model, OwnerModel):
            if request.user.is_superuser:
                return queryset
            else:
                return queryset.filter(model_owner__id=request.user.id)        
        return queryset
                
    def delete_model(self, request, obj):
        if issubclass(type(obj), OwnerModel):
            obj.delete(request=request)
        else:
            obj.delete()
            
    def has_change_permission(self, request, obj=None):        
        sp = super(BaseModelAdmin, self).has_change_permission(request)        
        return sp if not issubclass(type(obj), OwnerModel) else (
            has_permissions(request, obj, 'edit') if obj else sp
        )

    def has_delete_permission(self, request, obj=None):
        sp = super(BaseModelAdmin, self).has_change_permission(request)        
        return sp if not issubclass(type(obj), OwnerModel) else (
            has_permissions(request, obj, 'delete') if obj else sp
        )
            
    def get_changelist(self, request, **kwargs):
        return CoreChangeList
      
class BaseTabularInline(admin.TabularInline):
    actions = [delete_selected]
    formset = CoreBaseInlineFormSet
        
    def save_model(self, request, obj, form, change):
        if issubclass(type(obj), OwnerModel):
            obj.save(request=request)
        else:
            obj.save()      
    
        
    def has_change_permission(self, request, obj=None):
        sp = super(BaseTabularInline, self).has_change_permission(request)        
        return sp if not issubclass(type(obj), OwnerModel) else (
            has_permissions(request, obj, 'edit') if obj else sp
        )

    def has_delete_permission(self, request, obj=None):
        sp = super(BaseTabularInline, self).has_change_permission(request)        
        return sp if not issubclass(type(obj), OwnerModel) else (
            has_permissions(request, obj, 'delete') if obj else sp
        )
        
class BaseStackedInline(admin.StackedInline):
    actions = [delete_selected]
    formset = CoreBaseInlineFormSet
    
    def save_model(self, request, obj, form, change):
        print "NES"
        if issubclass(type(obj), OwnerModel):
            obj.save(request=request)
        else:
            obj.save()      
            
    def has_change_permission(self, request, obj=None):        
        sp = super(BaseStackedInline, self).has_change_permission(request)        
        return sp if not issubclass(type(obj), OwnerModel) else (
            has_permissions(request, obj, 'edit') if obj else sp
        )
    def has_delete_permission(self, request, obj=None):
        sp = super(BaseStackedInline, self).has_change_permission(request)        
        return sp if not issubclass(type(obj), OwnerModel) else (
            has_permissions(request, obj, 'delete') if obj else sp
        )
    
for M in [models.Country, models.County, models.Province]:
    class ItemAdmin(BaseModelAdmin):
        list_display = [f.name for f in M._meta.fields if f.name not in (
            'model_owner', 'site', 'access_control_list'
        )]
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass
		