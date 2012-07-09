from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response, redirect

from django.template.defaultfilters import slugify
from django.template.context import RequestContext

from uhai.userprofile.forms import RoleChooserForm
from uhai.records.models import Diagnosis, TrackingRecord, TrackingField, TrackingEntry

from datetime import datetime

def index(request, template_name="", data={}):
	if request.user.is_authenticated():
		if not request.session.get('use_page_as'):
			request.session['use_page_as'] = slugify(request.user.profile.main_role)
		else:
			if request.session.get('use_page_as') == 'patient':
				diagnoses = Diagnosis.objects.filter(approved=True, encounter__user=request.user.patient_set.get())		
				tracking_records = list(TrackingRecord.objects.filter(diagnosis__id__in=[diagnosis.problem.id for diagnosis in diagnoses]))
				vitals = list(TrackingRecord.objects.filter(slug__in=['blood-pressure', 'resting-heart-rate', 'temperature-oral']))
				tracking_records += vitals
				tracking_records = set(tracking_records)

				def getitems(tracking_record, ds={}):			
					tfq = tracking_record.trackingfield_set.all()		
					teq = TrackingEntry.objects.filter(field__in=TrackingField.objects.filter(tracking_record=tracking_record)).order_by('date_updated')
					if teq:
						yield ['Time'] + ['%s' % tf.name for tf in tfq]
						for te in teq:
							yield [te.date_updated.strftime('%d %b %I%p')] + [
								float(t.value) if t.value else 0 for t in teq.filter(shared_key=te.shared_key)
							]
						
				def getchartdata(_tuple):
					import json
					return {
						"title": _tuple[0].name,
						"label": _tuple[0].slug,
						"vaxis": _tuple[0].trackingfield_set.all() or '',
						"haxis": 'Time',
						"data" : json.dumps(list(_tuple[1]))
					}

				data['charts'] = map(getchartdata, [(t, getitems(t)) for t in tracking_records])
				data['items'] = tracking_records
			template_name = 'core/dashboard.html'
	else:
		template_name = 'index.html'	
	return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def use_as(request, type=None):
	if request.method == "POST":
		form = RoleChooserForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			profile = form.save()
			request.session['use_page_as'] = slugify(profile.main_role)
			return redirect('/')
	else:
		if type:
			request.session['use_page_as'] = type
		else:
			if not request.user.profile.main_role:
				data = {}
				template_name = 'use_as.html'	
				return render_to_response(template_name, data, context_instance=RequestContext(request))
	return redirect(request.META.get('HTTP_REFERER', '/'))
