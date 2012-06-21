from django.conf.urls.defaults import *
from django.contrib import admin

from django.db.models.base import ModelBase
from django.views.generic.base import TemplateView

urlpatterns = patterns('uhai.stats.views',
    url(r'^patients/delta.json', 'patient_delta', name='patient-stats')
)
