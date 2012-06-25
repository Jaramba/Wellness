from django.contrib import admin
import models
from django.db.models.base import ModelBase

model_classes = [x for x in models.__dict__.values()  if issubclass(type(x), ModelBase) and not x._meta.abstract]

for m in model_classes:
    class ItemAdmin(admin.ModelAdmin):
        model = m
        list_display = [f.name for f in m._meta.fields]
    try:
        admin.site.register(m, ItemAdmin)
    except:
        admin.sites.AlreadyRegistered