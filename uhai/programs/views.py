# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import model_view

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template.context import RequestContext

from django.http import Http404, HttpResponse

program = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programtype = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programworkflow = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programworkflowstate = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
enrolledprogram = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
questionnaire = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
questionaire = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def index(request, problem_type='', template_name = "programs/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def questionaire_view(request, pk=None, *args, **kwargs):
	model_obj = get_object_or_404(Questionnaire, pk=pk)
	questionsets = model_obj.questionset_set.all()
	questions = Question.objects.filter(questionset__in=questionsets)
	extra_data = locals()
	return model_view(request, model_obj=model_obj, extra_data=extra_data, *args, **kwargs)

@login_required
def responses(request, template_name=''):
	if request.method == 'POST':
		post = dict(request.POST.copy())
		type = 'error'
		message = 'There was an error sennding the response, please attempt the Survey again'				
		for k in post.keys():
			if k.startswith('question-'):
				response = Response.objects.get_or_create(
					answer_by=request.user.profile, 
					patient=request.user.profile.patient, 
					question_id=k.split('question-')[1], 
					value=post[k].pop()
				)
				type = 'success'
				message = 'You have successfully completed the Questionnaire'				
		
	template = '''
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal">&times;</button>
		</div>
		<div class="alert alert-%s">%s</div>
	''' % (type, message)
	return HttpResponse(template)

@login_required
def questionset(request, pk=None, questionnaire_pk=None, *args, **kwargs):
	try:
		qs = QuestionSet.pq_objects.filter(questionnaire__pk=questionnaire_pk)
		questionset = qs.get(pk=pk)
		previous = qs.order_by('-pk').filter(pk__lt=pk)[0:1]
		next     = qs.order_by('-pk').filter(pk__gt=pk)[0:1]
	except QuestionSet.DoesNotExist, e:		
		raise Http404(e)
	except ValueError,e:		
		raise Http404(e)
	return model_view(request, model_obj=questionset, extra_data=locals(), *args, **kwargs)
	