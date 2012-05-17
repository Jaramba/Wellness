from django import forms
from models import *

class MedicationIngredientForm(forms.ModelForm):
    class Meta:
        model = MedicationIngredient

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
