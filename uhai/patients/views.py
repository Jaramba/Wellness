# Create your views here.
from models import *
from forms import * 

from django.http import Http404
from django.contrib.auth.decorators import login_required

from uhai.core.views import *

@login_required
def patient(request, *args, **kwargs):
    try:
        if not kwargs.get('pk'):
            kwargs['pk'] = request.user.patient_set.get().pk
    except Patient.DoesNotExist:
        raise Http404()
    return user_model_view(request, max_pagination_items=3, *args, **kwargs)

@login_required
def patientemergencycontact(request, *args, **kwargs):
	def save_form(form, *args, **kwargs):
		contact = form.save(*args, **kwargs)
		contact.patient = request.user
		contact.save()
		
		return contact
	return model_view(request, save_form=save_form, *args, **kwargs)

@login_required
def relationship(request, queryset=None, *args, **kwargs):
    queryset = Relationship.objects.filter(person_a=request.user.patient_set.get())
    return model_view(request, queryset=queryset, *args, **kwargs)