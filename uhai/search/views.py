from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect

from django.http import HttpResponse
import simplejson

from django.db.models import Q

from uhai.patients.models import Patient

@login_required
def index(request, template_name='search/index.html', data={}):
	if request.method == "GET":
		q = request.REQUEST.get('q', None)
		q = q if q else request.REQUEST.get('query', None)
		results = []
		if q:
			if request.REQUEST.get('users', '').lower() == "yes":
				item = q
				results = Patient.objects.defer('user').filter(
					Q(user__userprofile__first_name__icontains=item)  |
					Q(user__userprofile__middle_name__icontains=item) |
					Q(user__userprofile__last_name__icontains=item)
				)
				
				data['patients'] = results
				data['q'] = q
						
			if request.REQUEST.get('jq', '') or request.is_ajax():
				suggestions = []
				
				for patient in results:
					profile = patient.user.profile
					suggestions.append('%s %s %s' % (profile.first_name, profile.middle_name, profile.last_name))					
				
				_data = suggestions = sorted(list(set(suggestions)))
				
				to_json = {
					'query': q,
					'suggestions': suggestions,
					'data': _data
				}
				return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
			else:
				page = request.REQUEST.get('page', 1)
				paginator = Paginator(results, 10)
				template_name='search/results.html'
				
				try:
					patients = paginator.page(page)
				except PageNotAnInteger:
					patients = paginator.page(1)
				except EmptyPage:
					patients = paginator.page(paginator.num_pages)				
			
	return render_to_response(template_name, data, context_instance= RequestContext(request))
