from models import *
from django import forms
from django.contrib.auth.models import User

class DoctorAdminForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		initial = {
#			'first_name':self.instance.user.first_name,
#			'last_name':self.instance.user.last_name,
#			'email':self.instance.user.email
		}
		return super(DoctorAdminForm, self).__init__(initial=initial, *args, **kwargs)
	
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	mobile_phone = forms.RegexField(r'\+2547\d{8}')
	home_phone = forms.RegexField(r'\+2547\d{8}')
	
	class Meta:
		model = Doctor
		fields = [
			'title',
			'first_name', 
			'middle_name', 
			'last_name', 
			'email',
			'mobile_phone',
			'home_phone',
			'work_phone',
			'postal_address',
			'photo',
			'gender',
			'country',
			'nationality',
			'user',
		]
		exclude = ['user']
	
	def save(self, commit=True):
		user = self.instance.user
		
		user.first_name = self.cleaned_data.get('first_name')
		user.middle_name = self.cleaned_data.get('middle_name')
		user.last_name = self.cleaned_data.get('last_name')
		
		user.save()
		
		return super(DoctorAdminForm, self).save(commit=commit)

class DoctorForm(DoctorAdminForm):
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
		
		return super(DoctorForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model = Doctor
		exclude = ['user','date_edited', 'date_created']
