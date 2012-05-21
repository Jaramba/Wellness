from django import forms
from models import *
from uni_form.helper import FormHelper
from uni_form.layout import *

class EncounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        layout = Layout(
            Div(HTML('<h2 class="form_title">Create Encounter</h2>'), css_class="form_title_div"),
            Row(Column('patient')),
            Row(Column('observation_notes')),
            Row(Column('encounter_provider')),
            Row(Column('encounter_date')),
            Row(Column('type')),
            Row(Column('visit')),
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
        
class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(''),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        self.helper.add_layout(self.layout)
        super(OrderForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Order
        
class VisitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'visit-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Row(Column('patient')),
            Row(Column('type')),
            Row(Column('indication_notes')),
            Row(Column('location')),
            Row(Column('start_time')),
            Row(Column('stop_time')),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        
        self.helper.add_layout(self.layout)
        super(VisitForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Visit
        
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

class TrackingRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(''),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        self.helper.add_layout(self.layout)
        super(TrackingRecordForm, self).__init__(*args, **kwargs)
    class Meta:
        model = TrackingRecord
        
class PatientTrackingRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(''),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        self.helper.add_layout(self.layout)
        super(PatientTrackingRecordForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = PatientTrackingRecord
        
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
            Row(Column('notes')),
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
        exclude = ['patient', 'attachments']
        
