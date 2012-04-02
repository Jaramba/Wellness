from django import forms
from models import *

class TrackingItemForm(forms.ModelForm):
    class Meta:
        model = TrackingItem
        exclude = ['user']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
