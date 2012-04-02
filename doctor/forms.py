from models import *
from django import forms

class DoctorAdminForm(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	
	class Meta:
		model = Doctor
		sequence = ['first_name', 'middle_name', 'last_name', 'email']
		exclude = ['user']

class DoctorForm(DoctorAdminForm):
	class Meta:
		model = Doctor
		sequence = ['first_name', 'middle_name', 'last_name', 'email']
		exclude = ['user']
