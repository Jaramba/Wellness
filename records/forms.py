from django import forms
from models import *
from uni_form.helper import FormHelper
from uni_form.layout import *

class EncounterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.layout = Layout(
            Div('', css_class='clearfix'),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        super(EncounterForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Encounter
        
class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div('', css_class='clearfix'),
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
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div('patient', css_class='clearfix'),
            Div('type', css_class='clearfix'),
            Div('indication_notes', css_class='clearfix'),
            Div('location', css_class='clearfix'),
            Div('start_time', css_class='clearfix'),
            Div('stop_time', css_class='clearfix'),
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
        self.layout = Layout(
            Div('', css_class='clearfix'),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        super(ProblemForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Problem
        
class TrackingFieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.layout = Layout(
            Div('', css_class='clearfix'),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        super(TrackingFieldForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = TrackingField
        
class ImmunizationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.layout = Layout(
            Div('', css_class='clearfix'),
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        )
        super(ImmunizationForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Immunization
        
