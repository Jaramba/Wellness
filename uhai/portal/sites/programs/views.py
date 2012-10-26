# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required

from uhai.portal.api.core.views import *

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils.http import urlquote
from email_extras.utils import send_mail_template

from signals import questionnaire_invalid, questionnaire_valid

from django.http import Http404, HttpResponse

@login_required
def index(request, problem_type='', template_name = "programs/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))

def questionnaire_detail(request, slug, QuestionnaireType=Questionnaire, 
    QuestionnaireTypeForm=QuestionnaireForm, template="questionnaires/questionnaire_%sdetail.html"):
	"""
	Display a built questionnaire and handle submission.
	"""
    
	published = QuestionnaireType.objects.published(for_user=request.user)
	questionnaire = get_object_or_404(published, slug=slug)
	if questionnaire.login_required and not request.user.is_authenticated():
		return redirect("%s?%s=%s" % (settings.LOGIN_URL, REDIRECT_FIELD_NAME,
						urlquote(request.get_full_path())))
	request_context = RequestContext(request)
	page = request.REQUEST.get('page',0)
	if request.method == "GET":
		questionnaireform = QuestionnaireTypeForm(
			questionnaire, request_context, 
			request.POST or None, request.FILES or None,
			page=page
		)
	else:
		questionnaireform = QuestionnaireTypeForm(
			questionnaire, request_context, 
			request.POST or None, request.FILES or None,
			paginate=False
		)
		if not questionnaireform.is_valid():
			questionnaire_invalid.send(sender=request, form=questionnaireform)
		else:
			entry = questionnaireform.save(request=request)
			subject = questionnaire.email_subject
			if not subject:
				subject = "%s - %s" % (questionnaire.title, entry.entry_time)
			fields = []
			for (k, v) in questionnaireform.fields.items():
				value = questionnaireform.cleaned_data[k]
				if isinstance(value, list):
					value = ", ".join([i.strip() for i in value])
				fields.append((v.label, value))
			context = {
				"fields": fields,
				"message": questionnaire.email_message,
				"request": request,
			}
			email_from = questionnaire.email_from or settings.DEFAULT_FROM_EMAIL
			email_to = questionnaireform.email_to()
			if email_to and questionnaire.send_email:
				send_mail_template(subject, "questionnaire_response", email_from,
								   email_to, context=context,
								   fail_silently=settings.DEBUG)
			email_copies = [e.strip() for e in questionnaire.email_copies.split(",")
							if e.strip()]
			if email_copies:
				if email_to and settings.SEND_FROM_SUBMITTER:
					# Send from the email entered.
					email_from = email_to
				attachments = []
				for f in questionnaireform.files.values():
					f.seek(0)
					attachments.append((f.name, f.read()))
				send_mail_template(subject, "questionnaire_response", email_from,
								   email_copies, context=context,
								   attachments=attachments,
								   fail_silently=settings.DEBUG)
			questionnaire_valid.send(sender=request, form=questionnaireform, entry=entry)
			return redirect(reverse_full("my-portal", "questionnaire_sent", view_kwargs={"slug": questionnaire.slug}))
	context = {"questionnaire": questionnaire}
	context["form"] = questionnaireform if page else None
	return render_to_response(template % ("" if not request.is_ajax() else "simple_"), context, request_context)


def questionnaire_sent(request, slug, template="questionnaires/questionnaire_%ssent.html"):
    """
    Show the response message.
    """
    published = Questionnaire.objects.published(for_user=request.user)
    questionnaire = get_object_or_404(published, slug=slug)
    context = {"questionnaire": questionnaire}
    return render_to_response(template % ("" if not request.is_ajax() else "simple_"), context, RequestContext(request))
