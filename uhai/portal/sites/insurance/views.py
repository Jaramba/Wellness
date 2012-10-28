# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.utils.views import *

employercompany = login_required(lambda request, *args, **kwargs: model_view(request, context_object_name_plural=lambda obj:"companies", *args, **kwargs))
