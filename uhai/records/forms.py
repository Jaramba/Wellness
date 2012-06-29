from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class EncounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Create Encounter</legend>')),
            Row(Column('patient'), Column('patient_complience')),       
            Row(Column('type')),
            Row(Column('location')),
            Row(Column('encounter_date')),
            Row(Column('start_time'), Column('end_time')),
            Row(Column('observation_notes')),
            
            Row(
				Div(
					Submit('send', 'Send', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(EncounterForm, self).__init__(*args, **kwargs)
        
    class Meta:
		model = Encounter
		exclude = ['provider']
		widgets = {
			'observation_notes' : forms.Textarea,
		}
		
class EncounterPatientForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '#'

		self.layout = Layout(
			Div(HTML('<legend>Enter Encounter</legend>')),
			Row(Column('type')),
			Row(Column('provider')),
			Row(Column('location')),
			Row(Column('encounter_date')),
			Row(Column('start_time'), Column('end_time')),
			Row(Column('observation_notes'), css_class="textarea"),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
		)        
		self.helper.add_layout(self.layout)
		super(EncounterPatientForm, self).__init__(*args, **kwargs)
    
	class Meta:
		model = Encounter
		exclude = ['patient', 'patient_complience']
		widgets = {
			'observation_notes' : forms.Textarea,
		}

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Order</legend>')),
            Row(Column('encounter')),
            Row(Column('discontinued')),
            Row(Column('instructions')),
            Row(Column('concept_notes')),
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(OrderForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Order
        exclude = ['discontinued_reason']
        widgets = {
            'instructions': forms.Textarea,
            'concept_notes': forms.Textarea
        }
                
class ProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Create Problem</legend>')),
            Row(Column('code')),
            Row(Column('type')),
            Row(Column('source')),
            Row(Column('status')),
            Row(Column('notes')),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        
        self.helper.add_layout(self.layout)
        super(ProblemForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Problem
        exclude = ['patient', 'attachments', 'name']
        widgets = {
            'side_effects' : forms.Textarea
        }
		
class TrackingFieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
        )
        
        self.helper.add_layout(self.layout)
        super(TrackingFieldForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = TrackingField
        
class ImmunizationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Create Immunization</legend>')),
            Row(Column('name')),
            Row(Column('code')),
            Row(Column('vaccine'), Column('brand_name')),
            Row(Column('duration_of_protection')),
            Row(Column('mode_of_delivery')),
            Row(Column('site')),
            Row(Column('expiry_date'), Column('practice_date')),
            Row(Column('follow_up_date')),
            Row(Column('notes')),
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
        exclude = ['patient']
        widgets = {
            'notes': forms.Textarea
        }
        
class DiagnosisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column('problem')),
            Row(Column('approved')),
            Row(Column('encounter')),
            Row(Column('notes')),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(DiagnosisForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Diagnosis
        exclude = ['patient']
        widgets = {
            'notes': forms.Textarea
        }


class ProblemTestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column('name')),
            Row(Column('problem')),
            Row(Column('expected_outcomes')),
            Row(Column('details')),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(ProblemTestForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = ProblemTest
        exclude = ['patient', 'slug', 'date_added']
        widgets = {
            'expected_outcomes': forms.Textarea,
            'details': forms.Textarea
        }


class EncounterTestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column('name')),
            Row(Column('encounter')),
            Row(Column('test')),
            Row(Column('date_administered')),
            Row(Column('notes')),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(EncounterTestForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = EncounterTest
        exclude = ['patient', 'slug', 'date_added']
        widgets = {
            'notes': forms.Textarea,
        }

class EncounterTestResultForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column('name')),
            Row(Column('encounter_test')),
            Row(Column('inference')),
            Row(Column('notes')),
            Row(Column('notes')),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(EncounterTestResultForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = EncounterTest
        exclude = ['date_added']
        widgets = {
            'notes': forms.Textarea
        }

		