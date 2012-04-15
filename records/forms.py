from django import forms
from models import *
from uni_form.helper import FormHelper
from uni_form.layout import *

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        layout = [
            Div(f.name, css_class='clearfix') for f in Encounter._meta.fields if not f.name in ['id']
        ]
        layout += [
            Div(
                Div(
                    Submit('Save', 'Save Changes', css_class='button blue'),
                    css_class='input no-label'
                ),
                css_class='clearfix grey-highlight'
            )
        ]
        
        layout = Layout(
            *layout
        )
        
        self.helper.add_layout(layout)
        
class EncounterForm(BaseForm):
    class Meta:
        model = Encounter
        
class OrderForm(BaseForm):
    class Meta:
        model = Order
        
class VisitForm(BaseForm):
    class Meta:
        model = Visit
        
class ProblemForm(BaseForm):
    class Meta:
        model = Problem
        
class TrackingFieldForm(BaseForm):
    class Meta:
        model = TrackingField
        
class ImmunizationForm(BaseForm):
    class Meta:
        model = Immunization
        
