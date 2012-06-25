from django import forms
from django.utils.crypto import get_random_string

from models import *

from crispy_forms.helper import *
from crispy_forms.layout import *

from utils import perform_raw_sql
from datetime import datetime

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship

class RelationshipTypeForm(forms.ModelForm):
    class Meta:
        model = RelationshipType
