from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect

from django.db.models import Q

from uhai.patients.models import Patient

@login_required
def index(request, template_name='search/index.html', data={}):
	if request.method == "GET":
		if request.REQUEST.get('q', None):
			q = request.REQUEST.get('q')
			template_name='search/results.html'
			
			page = request.REQUEST.get('page', 1)
			patients = Patient.objects.filter(
				Q(user__userprofile__first_name__icontains=q) | 
				Q(user__userprofile__middle_name__icontains=q) |
				Q(user__userprofile__last_name__icontains=q)
			)
			paginator = Paginator(patients, 10)

			try:
				patients = paginator.page(page)
			except PageNotAnInteger:
				patients = paginator.page(1)
			except EmptyPage:
				patients = paginator.page(paginator.num_pages)

			data['patients'] = patients
			data['q'] = q
					
	return render_to_response(template_name, data, context_instance= RequestContext(request))
	