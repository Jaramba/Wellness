from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect

from uhai.records.models import Diagnosis, TrackingRecord, TrackingField, TrackingEntry
import json
from datetime import datetime

def index(request, template_name="", data={}):
	if request.user.is_authenticated():
		template_name = 'core/dashboard.html'
		
		diagnoses = Diagnosis.objects.filter(approved=True, encounter__user=request.user.patient)		
		tracking_records = list(TrackingRecord.objects.filter(diagnosis__id__in=[diagnosis.problem.id for diagnosis in diagnoses]))
		vitals = list(TrackingRecord.objects.filter(slug__in=['temperature-oral', 'resting-heart-rate', 'blood-pressure']))
		tracking_records += vitals
		tracking_records = set(tracking_records)
		
		def getitems(tracking_record, ds={}):
			teq = TrackingEntry.objects.filter(field__in=TrackingField.objects.filter(tracking_record=tracking_record))
			for d in teq.dates('date_updated', 'month'):
				yield ([d.strftime('%d-%m-%Y %H:00')] + [te.value for te in teq])

		data['charts'] = [{
			"label": t.slug,
			"data" : json.dumps([(['Time'] + [tf.name for tf in t.trackingfield_set.all()]), list(getitems(t))])
		} for t in tracking_records]
		
		data['items'] = tracking_records
	else:
		template_name = 'index.html'	
	return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required 
def use_as(request, type):
	request.session['use_page_as'] = type
	return redirect('/')
