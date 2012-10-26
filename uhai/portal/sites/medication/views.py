# Create your views here.
from models import *
from forms import * 

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from uhai.portal.api.core.views import *

from django.http import Http404
from django.shortcuts import get_object_or_404

from uhai.portal.sites.patients.models import Patient
from django.contrib.auth.models import User

@login_required
def prescription(request, user_pk=None, *args, **kwargs): 
	def save_form(form, *args, **kwargs):
		contact = form.save(*args, **kwargs)
		obj.user = request.user
		obj.end_time = obj.follow_up_date = obj.start_time
		obj.text = 'Vaccination for %s' % obj.user
		obj.save()
		return obj
	kwargs['save_form'] = save_form
	return user_model_view(request, *args, **kwargs)

@login_required
def immunization(request, user_pk=None, *args, **kwargs):
	def save_form(form, *args, **kwargs):
		obj = form.save(*args, **kwargs)
		obj.user = request.user
		obj.end_time = obj.follow_up_date = obj.start_time
		obj.text = 'Vaccination for %s' % obj.user
		obj.save()
		return obj
	kwargs['save_form'] = save_form
	return user_model_view(request, *args, **kwargs)
