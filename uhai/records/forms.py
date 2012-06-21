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
        
        layout = Layout(
            Div(HTML('<h2 class="form_title">Create Encounter</h2>'), css_class="form_title_div"),
            Row(Column('patient'), Column('patient_complience')),       
            Row(Column('type')),   
            Row(Column('provider')),
            Row(Column('location')),
            Row(Column('encounter_date')),
            Row(Column('start_time'), Column('end_time')),
            Row('observation_notes'),
            
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        super(EncounterForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Encounter
        widgets = {
            'observation_notes' : forms.Textarea
        }
        
class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<h2 class="form_title">Add Order</h2>'), css_class="form_title_div"),
            Row(Column('encounter')),
            Row(Column('discontinued')),
            Row('instructions'),
            Row('concept_notes'),
            Div(
                Div(
                    Submit('Save', 'Save Changes'),
                ),
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
            Div(HTML('<h2 class="form_title">Create Problem</h2>'), css_class="form_title_div"),
            Row(Column('code')),
            Row(Column('type')),
            Row(Column('source')),
            Row(Column('status')),
            Row(Column('notes')),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
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
            Div(HTML('<h2 class="form_title">Create Immunization</h2>'), css_class="form_title_div"),
            Row(Column('name')),
            Row(Column('code')),
            Row(Column('vaccine')),
            Row(Column('brand_name')),
            Row(Column('lot_number')),
            Row(Column('route')),
            Row(Column('site')),
            Row(Column('expiry_date')),
            Row(Column('practice_date')),
            Row(Column('follow_up_date')),
            Row('notes'),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
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
            Div(HTML('<h2 class="form_title">Add Diagnosis</h2>'), css_class="form_title_div"),
            Row(Column('problem')),
            Row(Column('approved')),
            Row(Column('encounter')),
            Row(Column('notes')),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
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
            Div(HTML('<h2 class="form_title">Add Diagnosis</h2>'), css_class="form_title_div"),
            Row(Column('name')),
            Row(Column('problem')),
            Row(Column('expected_outcomes')),
            Row(Column('details')),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
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
            Div(HTML('<h2 class="form_title">Add Diagnosis</h2>'), css_class="form_title_div"),
            Row(Column('name')),
            Row(Column('encounter')),
            Row(Column('test')),
            Row(Column('date_administered')),
            Row('notes'),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
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
            Div(HTML('<h2 class="form_title">Add Diagnosis</h2>'), css_class="form_title_div"),
            Row(Column('name')),
            Row(Column('encounter_test')),
            Row(Column('inference')),
            Row(Column('notes')),
            Row('notes'),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
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
