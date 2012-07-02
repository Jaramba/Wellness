from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(Column('title')),
            Row(Column('first_name'),Column('middle_name'),Column('last_name')),
			Row(Column('national_id')),
            Row(Column('postal_code')),
            Row(Column('home_phone'),Column('mobile_phone'),Column('work_phone')),
			Row(Column('blood_group')),
            Row(Column('postal_address')),
            Row(Column('gender'), Column('date_of_birth')),
            Row(Column('country'), Column('province'), Column('county'), Column('village')),            
            Row(Column('weight'), Column('height')),
            Row(Column('employer')),
            Row(Column('doctor')),            
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        
        return super(PatientForm, self).__init__(*args, **kwargs)
    
    gender = forms.ChoiceField(
        choices=(('','Select your gender'),('male','Male'),('female','Female')), 
        help_text="Whats your gender?"
    )
    date_of_birth = forms.DateField(
		input_formats=['%d/%m/%Y','%Y-%m-%d'], required=False, 
		help_text='The Patient\'s indicated date of birth'
	)
    
    class Meta:
		model = Patient
		exclude = [
			'insurance', 'relationship', 
			'latitude', 'longitude', 'photo',
			'user', 'patient_number'
		]

class PatientEmergencyContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'patient-form'
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '.'
		
		layout = Layout(
			Div(HTML('<legend>Enter Emergency Contact</legend>')),
			Row(Column(Field('full_name', css_class='span5'))),
			Row(Column(Field('email', css_class='span4'))),
			Row(Column(Field('mobile_phone', css_class='span3'))),
			Row(Column(Field('home_phone', css_class='span3'))),
			Row(Column(Field('work_phone', css_class='span3'))),
			Row(Column(Field('postal_code', css_class='span3'))),
			Row(Column('national_id')),
			Row(Column('next_of_kin')),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
		)
		self.helper.add_layout(layout)
		
		return super(PatientEmergencyContactForm, self).__init__(*args, **kwargs)

	class Meta:
		model = PatientEmergencyContact
		exclude = ['patient']
