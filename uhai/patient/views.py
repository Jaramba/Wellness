# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import model_view

patient = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def relationship(request, queryset=None, *args, **kwargs):
    queryset = Relationship.objects.filter(person_a=request.user.profile.patient)
    return model_view(request, queryset=queryset, *args, **kwargs)

relationshiptype = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))