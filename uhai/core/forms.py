from django import forms
from django.contrib.sites.models import Site

from models import *

from crispy_forms.helper import *
from crispy_forms.layout import *

from utils import perform_raw_sql
from datetime import datetime

class BaseModelForm(forms.ModelForm):        
    def save(self, commit=False, request=None, *args, **kwargs):
        obj = super(BaseModelForm, self).save(commit=commit)
        if commit:
            obj.save(request=request, *args, **kwargs)                
        return obj
