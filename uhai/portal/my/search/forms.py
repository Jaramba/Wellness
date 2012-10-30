from django import forms
from uhai.portal.my.patients.models import Patient

class SearchPatientForm(forms.Form):
	patient = forms.ModelChoiceField(
		queryset=Patient.objects.all(), 
		empty_label=u"", 
		label="Patient",
	)