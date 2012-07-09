# Create your views here.
from models import *
from forms import * 

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from uhai.core.views import model_view, user_model_view, role_model_view

from django.http import Http404
from django.shortcuts import get_object_or_404

from uhai.patients.models import Patient
from django.contrib.auth.models import User

medication = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))

@login_required
def prescription(request, user_pk=None, *args, **kwargs): 
	def save_form(form, commit=False):
		obj = form.save(commit=commit)
		obj.user = request.user
		obj.end_time = obj.follow_up_date = obj.start_time
		obj.text = 'Vaccination for %s' % obj.user
		obj.save()
		return obj
	kwargs['save_form'] = save_form
	return user_model_view(request, *args, **kwargs)

@login_required
def immunization(request, user_pk=None, *args, **kwargs):
	def save_form(form, commit=False):
		obj = form.save(commit=commit)
		obj.user = request.user
		obj.end_time = obj.follow_up_date = obj.start_time
		obj.text = 'Vaccination for %s' % obj.user
		obj.save()
		return obj
	kwargs['save_form'] = save_form
	return user_model_view(request, *args, **kwargs)
