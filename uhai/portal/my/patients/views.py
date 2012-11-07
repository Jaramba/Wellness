# Create your views here.
from models import *
from forms import * 

from django.http import Http404
from django.contrib.auth.decorators import login_required

from uhai.core.views import *
from uhai.portal.my.providers.models import PatientProvider

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
    queryset = Relationship.objects.filter(person_a=request.user)
    return model_view(request, queryset=queryset, *args, **kwargs)

@login_required
def dependents(request, template_name="patients/dependents.html", data={}, *args, **kwargs):
    dependent_relationships = Relationship.objects.filter(relationship__dependent=True)
    data['dependent_relationships'] = dependent_relationships
    return render_to_response(template_name, data, context_instance=RequestContext(request))

@login_required
def doctors(request, template_name="patients/doctors.html", data={}, *args, **kwargs):
    data['doctors'] = PatientProvider.objects.filter(patient=request.user.patient_set.get())
    return render_to_response(template_name, data, context_instance=RequestContext(request))