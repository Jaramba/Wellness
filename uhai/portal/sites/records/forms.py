from django import forms
from models import (
    Encounter, EncounterTest, Order,
    ProblemTest, Problem, ProblemTest,
    Diagnosis
)

from uhai.portal.api.core.forms import BaseModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

from django.contrib.auth.models import User

class EncounterForm(BaseModelForm):
	user = forms.ModelChoiceField(queryset=User.objects.filter(patient__pk__isnull=False), empty_label=u"", label="Patient")
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '#'
		
		self.layout = Layout(
			Div(HTML('<legend>Create Encounter</legend>')),
			Row(Column(Field('user', css_class="span4"))),
			Row(Column(Field('frequency', css_class="span2"))),	
			Row(Column(Field('patient_complience'))),
			Row(Column(Field('type'))),
			Row(Column(Field('completed'))),
			Row(Column(Field('location', css_class="span4"))),
			Row(Column(Field('start_time'))),
			Row(Column(Field('end_time'))),
			Row(Field('observation_notes'), css_class='textarea-column'),
			
			Row(
				Div(
					Submit('send', 'Send', css_class='btn-primary'),
					css_class='form-actions'
				)
			)
		)
		self.helper.add_layout(self.layout)
		super(EncounterForm, self).__init__(*args, **kwargs)
		
	class Meta:
		model = Encounter
		exclude = ['provider', 'text']
		widgets = {
			'observation_notes' : forms.Textarea,
		}
		
	def save(self, commit=True):
		obj = super(EncounterForm, self).save(commit=False)
		obj.text = 'Appointment with %s' % obj.user
		
		if commit:
			obj.save()
		return obj
		
class PatientEncounterForm(BaseModelForm):
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '#'

		self.layout = Layout(
			Div(HTML('<legend>Enter Encounter</legend>')),
            Row(Column(Field('frequency', css_class='span2'))),
			Row(Column(Field('type', css_class='span3'))),
			Row(Column(Field('provider', css_class='span4'))),
			Row(Column(Field('location', css_class='span4'))),
			Row(Column(Field('completed'))),
			Row(Column(Field('start_time'))),
			Row(Column(Field('end_time'))),
			Row(Field('observation_notes'), css_class="textarea-column"),
			
			Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions'
				)
			)
		)
		self.helper.add_layout(self.layout)
		super(PatientEncounterForm, self).__init__(*args, **kwargs)
    
	class Meta:
		model = Encounter
		exclude = ['user', 'patient_complience', 'text']
		widgets = {
			'observation_notes' : forms.Textarea,
		}

class OrderForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Order</legend>')),
            Row(Column(Field('encounter'))),
            Row(Column(Field('discontinued'))),
            Row(Column('instructions', css_class='textarea-column')),
            Row(Column('concept_notes'), css_class='textarea-column'),
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
                
class ProblemForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Create Problem</legend>')),
            Row(Column(Field('code'))),
            Row(Column(Field('type'))),
            Row(Column(Field('source'))),
            Row(Column(Field('status'))),
            Row(Column('notes'), css_class='textarea-column'),
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
		
class DiagnosisForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column(Field('problem'))),
            Row(Column(Field('approved'))),
            Row(Column(Field('encounter'))),
            Row(Field('notes'), css_class='textarea-column'),
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


class ProblemTestForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column(Field('name'))),
            Row(Column(Field('problem'))),
            Row(Column(Field('expected_outcomes'))),
            Row(Column('details'), css_class='textarea-column'),
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


class EncounterTestForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column(Field('name'))),
            Row(Column(Field('encounter'))),
            Row(Column(Field('test'))),
            Row(Column(Field('date_administered'))),
            Row(Column('notes'), css_class='textarea-column'),
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

class EncounterTestResultForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Add Diagnosis</legend>')),
            Row(Column(Field('name'))),
            Row(Column(Field('encounter_test'))),
            Row(Column(Field('inference'))),
            Row(Column('notes'), css_class='textarea-column'),
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
