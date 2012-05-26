from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.shortcuts import render_to_response

@login_required
def index(request):
    data = {}
    template_name = "core/dashboard.html"
    return render_to_response(template_name, data, context_instance= RequestContext(request))

