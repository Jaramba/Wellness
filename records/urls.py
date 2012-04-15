from django.conf.urls.defaults import *
from django.contrib import admin

from models import (Encounter, Order, Problem, Immunization, Visit)
from django.db.models.base import ModelBase

urlpatterns = patterns('')

for M in (Encounter, Order, Problem, Immunization, Visit):
    #The app itself
    model_name = M.__name__.lower()
    urlpatterns += patterns('records.views',
        url(r'^%s/create/$' % model_name, model_name, {'action' : 'create', 'model_class':M}, name=' %s-create' % model_name),
        url(r'^%s/list/$' % model_name, model_name, {'action' : 'list', 'model_class':M}, name=' %s-list' % model_name),
        url(r'^%s/(?P<pk>[-\w]+)/edit/$' % model_name, model_name, {'action' : 'edit', 'model_class':M}, name=' %s-edit' % model_name),
        url(r'^%s/(?P<pk>[-\w]+)/delete/$' % model_name, model_name, {'action' : 'delete', 'model_class':M}, name=' %s-delete' % model_name),
        url(r'^%s/(?P<pk>[-\w]+)/$' % model_name, model_name, {'action' : 'detail', 'model_class':M}, name=' %s-detail' % model_name),
    )

