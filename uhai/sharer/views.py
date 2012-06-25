from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpRequest, HttpResponseRedirect

from django.views.decorators.csrf import csrf_protect
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import render_to_response, get_object_or_404
from models import *

@login_required
@csrf_protect
def sharer(request, template_name=None, action="list", app_label=None, model=None, pk=None, data={}):
	if request.method == "POST":
		ct = get_object_or_404(ContentType, app_label=app_label, model=model)
		for ob in ct.model_class().objects.all():
			sharer, created = Sharer.objects.get_or_create(content_type=ct, object_pk=ob.pk, shared_by=request.user, shared_to=request.user)

		return HttpResponseRedirect('/')
	else:
		if action=="list":
			data['sharerequests'] = ShareRequest.objects.filter(requestee=request.user)
	return render_to_response(template_name, data, context_instance=RequestContext(request))
