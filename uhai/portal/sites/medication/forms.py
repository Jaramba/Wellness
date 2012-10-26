from uhai.core.forms import *
from models import (
    Medication, 
    Immunization,
    Prescription
)

from crispy_forms.helper import *
from crispy_forms.layout import *

from django.contrib.auth.models import User

class MedicationForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-insurance-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<legend>Enter Medication</legend>')),
            Row(Column(Field('name', css_class="span6"))),
            Row(Column(Field('medication_type', css_class="span4"))), 
			Row(Column(Field('way_taken', css_class="span4"))),
            Row(Column(Field('min_daily_dose', css_class="span2"))), 
			Row(Column(Field('max_daily_dose', css_class="span2"))),
            Row(Column(Field('strength', css_class="span2"))), 
			Row(Column(Field('strength_unit', css_class="span3"))),
            Row(Field('side_effects') ,css_class="textarea-column"),
            
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(layout)

        return super(MedicationForm, self).__init__(*args, **kwargs)
    
	name = forms.CharField(required=False, help_text="Name of the insurance, if customised for the Patient.")
    
    class Meta:
        model = Medication
        exclude = ['patient']
        widgets = {
            'side_effects' : forms.Textarea
        }

class PrescriptionForm(BaseModelForm):
	user = forms.ModelChoiceField(queryset=User.objects.filter(patient__pk__isnull=False), empty_label=u"", label="Patient")
	start_time = forms.DateTimeField(label="Date Prescribed")
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'patient-insurance-form'
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '.'
		
		layout = Layout(
			Row(HTML('<legend>Add Prescription</legend>')),
			Row(Column(Field('user', css_class="span5"))),
			Row(Column(Field('provider', css_class="span5"))),
			Row(Column(Field('medication', css_class="span4"))),
			Row(Column(Field('quantity'))),
			Row(Column(Field('unit', css_class="span3"))),
			Row(Column(Field('frequency', css_class="span3"))),
			Row(Column(Field('completed'))),
			Row(Column(Field('start_time'))),
			Row(Field('reason'), css_class='textarea-column'),
			Row(HTML('<br/><br/>')),
			Row(Field('notes'), css_class='textarea-column'),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
		)
		self.helper.add_layout(layout)

		return super(PrescriptionForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Prescription
		exclude = ['end_time', 'text']
		widgets = {
			'reason' : forms.Textarea,
			'notes' : forms.Textarea
		}

class PatientPrescriptionForm(BaseModelForm):
	start_time = forms.DateTimeField(label="Date Prescribed")
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'patient-insurance-form'
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '.'
		
		layout = Layout(
			Row(HTML('<legend>Add Prescription</legend>')),
			Row(Column(Field('medication', css_class="span5"))),
			Row(Column(Field('provider', css_class="span5"))),
			Row(Column(Field('quantity', css_class="span1"))),
			Row(Column(Field('unit', css_class="span3"))),
			Row(Column(Field('frequency', css_class="span2"))),
			Row(Column(Field('completed'))),
			Row(Column(Field('start_time'))),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
		)
		self.helper.add_layout(layout)

		return super(PatientPrescriptionForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Prescription
		exclude = ['end_time', 'text', 'user', 'notes', 'reason']
		widgets = {
			'reason' : forms.Textarea,
			'notes' : forms.Textarea
		}
		
class ImmunizationForm(BaseModelForm):
	user = forms.ModelChoiceField(queryset=User.objects.filter(patient__pk__isnull=False), empty_label=u"", label="Patient")
	start_time = forms.DateTimeField(label="Date of Administered")
    	
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'problem-form'
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '.'

		self.layout = Layout(
			Div(HTML('<legend>Add Patient Immunization</legend>')),
			Row(Column(Field('user', css_class="span5"))),
			Row(Column(Field('code'))),
			
			Row(Column(Field('provider', css_class="span5"))),
			Row(Column(Field('frequency'))),
			
			Row(Column(Field('completed'))),
			Row(Column(Field('brand_name', css_class="span6"))),
			Row(Column(Field('duration_of_protection'))),
			Row(Column(Field('mode_of_delivery', css_class="span4"))),
			
			Row(Column(Field('start_time', css_class="span3"))),

			Row(Column(Field('expiry_date'))),
			Row(Column(Field('follow_up_date'))),
			
			Row(Field('notes'), css_class='textarea-column'),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
		)
		self.helper.add_layout(self.layout)
		super(ImmunizationForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Immunization
		exclude = ['text', 'end_time']
		widgets = {
			'notes': forms.Textarea
		}
	
	def save(self, commit=True, *args, **kwargs):
		obj = super(ImmunizationForm, self).save(commit=commit, *args, **kwargs)
        
		obj.end_time = obj.start_time
		obj.text = 'Vacination for %s' % obj.user
		
		if commit:
			obj.save()
		return obj

class PatientImmunizationForm(BaseModelForm):
	start_time = forms.DateTimeField(label="Date of Administered")
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'problem-form'
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '.'
		
		self.layout = Layout(
			Div(HTML('<legend>Add Immunization</legend>')),
			Row(Column(Field('provider', css_class="span5"))),
			Row(Column(Field('brand_name', css_class="span6"))),
			Row(Column(Field('mode_of_delivery', css_class="span4"))),
			
			Row(Column(Field('start_time', css_class="span3"))),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
		)
		self.helper.add_layout(self.layout)
		super(PatientImmunizationForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model = Immunization
		fields = ['provider', 'brand_name', 'mode_of_delivery', 'start_time']
