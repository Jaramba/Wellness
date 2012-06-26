from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class ReminderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = '%s-form' % self._meta.model._meta.object_name
		self.helper.form_class = 'general_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '#'

		layout = Layout(
			Div(HTML('<legend>Create Reminder</legend>'), css_class="form_title_div"),
			Row(Column('patient')),
			Row(Column('message')),
			Row(Column('frequency')),
			Row(Column('start_date'), Column('end_date')),
			
			Row(
				ButtonHolder(
					Submit('Save', 'Save Changes'),
				)
			)
		)
		self.helper.add_layout(layout)
		super(ReminderForm, self).__init__(*args, **kwargs)
        
    class Meta:
		model = Reminder
		widgets = {
			'message' : forms.Textarea
		}
		