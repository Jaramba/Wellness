from models import *
from django import forms
from django.contrib.auth.models import User

class HealthCareFacilityForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		return super(HealthCareFacilityForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model = HealthCareFacility

class HealthWorkerAdminForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		return super(HealthWorkerAdminForm, self).__init__(*args, **kwargs)
	
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	mobile_phone = forms.RegexField(r'\+2547\d{8}')
	home_phone = forms.RegexField(r'\+2547\d{8}')

	class Meta:
		model = HealthWorker
		fields = [
			'first_name', 
			'last_name', 
			'email',
			'mobile_phone',
			'home_phone',
		]
	
	def save(self, commit=True):
		user = self.instance.user
		
		user.first_name = self.cleaned_data.get('first_name')
		user.middle_name = self.cleaned_data.get('middle_name')
		user.last_name = self.cleaned_data.get('last_name')
		
		user.save()
		
		return super(HealthWorkerAdminForm, self).save(commit=commit)

class HealthWorkerForm(HealthWorkerAdminForm):
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'doctor-form'
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '.'
		
		layout = Layout(
		    Row(Column('photo')),
		    Row(Column('title')),
		    Row(Column('first_name'),Column('middle_name'),Column('last_name')),
		    Row(Column('email')),
		    Row(Column('mobile_phone'),Column('mobile_phone'),Column('work_phone')),
		    Row(Column('postal_address')),
		    Row(Column('gender')),
		    Row(Column('country'), Column('nationality')),
		    Row(
		        ButtonHolder(
		            Submit('Save', 'Save Changes'),
		        )
		    )
		)
		self.helper.add_layout(layout)
		
		return super(HealthWorkerForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model = HealthWorker
		exclude = ['user','date_edited', 'date_created']
