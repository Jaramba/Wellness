from django import forms
from models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        
class KinForm(forms.ModelForm):
    class Meta:
        model = Kin
        
class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact