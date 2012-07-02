# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import model_view

medication = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
prescription = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
immunization = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))