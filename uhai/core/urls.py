from django.conf.urls.defaults import *
from django.contrib import admin

from django.db.models.base import ModelBase
from django.views.generic.base import TemplateView
from django.template.defaultfilters import slugify

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='website/how_it_works.html'),name='providers'),
)
