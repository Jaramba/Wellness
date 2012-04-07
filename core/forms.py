from django.contrib.auth.forms import UserChangeForm
from django import forms

class CoreUserChangeForm(UserChangeForm):
	first_name = forms.CharField()
	middle_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField(label=("E-mail"), max_length=75)
	