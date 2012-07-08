# Create your views here.
from models import *
from forms import * 

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from uhai.core.views import model_view, user_model_view

from django.http import Http404
from django.shortcuts import get_object_or_404

from uhai.patients.models import Patient
from django.contrib.auth.models import User

medication = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def prescription(request, user_pk=None, *args, **kwargs): 
	if user_pk and not request.session.get('use_page_as') == 'patient':
		try:
			patient_profile = get_object_or_404(User, pk=user_pk).patient
			
			if kwargs['action'] in ('create', 'edit'):				
				kwargs['redirect_to'] = reverse('%s-list' % kwargs['queryset'].model.__name__.lower(), user_pk)
		except Patient.DoesNotExist:
			raise Http404('User #%s does not have patient profile active/activated' % user_pk)
	else:
		kwargs['queryset'] = kwargs['queryset'].filter(user=request.user)
		if kwargs['action'] in ('create', 'edit'):
			kwargs['redirect_to'] = reverse('%s-list' % kwargs['queryset'].model.__name__.lower(), user_pk)
	return model_view(request, *args, **kwargs)

@login_required
def immunization(request, user_pk=None, *args, **kwargs):
	def save_form(form, commit=False):
		obj = form.save(commit=commit)
		obj.user = request.user
		obj.end_time = obj.follow_up_date = obj.start_time
		obj.text = 'Vacination for %s' % obj.user
		obj.save()
		return obj
	kwargs['save_form'] = save_form
	return user_model_view(request, *args, **kwargs)
