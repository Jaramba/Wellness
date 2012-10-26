from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect

from django.template.defaultfilters import slugify
from django.template.context import RequestContext

from uhai.programs.models import DiagnosisQuestionnaire

@login_required
def switchboard(request, template_name='portal/my/switchboard.html', data={}):
    if not request.session.get('use_page_as'):
        request.session['use_page_as'] = slugify(request.user.profile.main_role)
    if request.session.get('use_page_as') == 'patient':pass
    data['diagnosisquestionnaires'] = DiagnosisQuestionnaire.objects.all()
    return render_to_response(template_name, data, context_instance= RequestContext(request))