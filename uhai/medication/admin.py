from django.contrib import admin

from django.forms.models import modelform_factory

from uhai.core.admin import BaseModelAdmin, BaseTabularInline

import models
import forms

from django.db.models.base import ModelBase

model_classes = [
    x for x in
    models.__dict__.values()
    if issubclass(type(x), ModelBase) and not x._meta.abstract
]

for M in model_classes:
    class ItemAdmin(BaseModelAdmin):
        #form = forms.__dict__.get(
        #    M.__name__ + 'Form',
        #    modelform_factory(M, form=forms.BaseModelForm)
        #)
        list_display = [f.name for f in M._meta.fields if not f.name in (
            'id', 'frequency', 'duration_of_protection', 'event_ptr', 
            'observation_notes', 'message', 'completed', 'location'
        )]
    try:
        admin.site.register(M, ItemAdmin)
    except:
        admin.sites.AlreadyRegistered
