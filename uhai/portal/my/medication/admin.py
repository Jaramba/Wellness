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
        list_display = [f.name for f in M._meta.fields if not f.name in (
            'id', 'frequency', 'duration_of_protection', 
            'observation_notes', 'message', 'completed', 'location',
            'model_owner', 'site', 'access_control_list', 'event_ptr'
        )
    ]
    try:
        admin.site.register(M, ItemAdmin)
    except:
        admin.sites.AlreadyRegistered
