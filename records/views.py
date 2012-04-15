# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from core.views import model_view

encounter = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
order = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
visit = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
problem = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
immunization = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
