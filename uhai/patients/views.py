# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import model_view

@login_required
def patient(request, *args, **kwargs):
	return model_view(request, max_pagination_items=4, *args, **kwargs)

@login_required
def patientemergencycontact(request, *args, **kwargs):
	def save_form(form):
		contact = form.save(commit=False)
		contact.patient = request.user
		contact.save()
		
		return contact
	return model_view(request, save_form=save_form, *args, **kwargs)

@login_required
def relationship(request, queryset=None, *args, **kwargs):
    queryset = Relationship.objects.filter(person_a=request.user.patient)
    return model_view(request, queryset=queryset, *args, **kwargs)