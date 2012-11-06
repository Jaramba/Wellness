from django.db.models.fields import Field
from django.db import models
from django.core import exceptions

import ast

class ACLField(Field):
    __metaclass__ = models.SubfieldBase
    description = "ACL Dictionary Object"
    default_error_messages = {
        'invalid': (u"'%s' value not a valid object."),
    }
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2000)
        super(ACLField, self).__init__(*args, **kwargs)
        
    def get_internal_type(self):
        return "CharField"

    def get_internal_type(self):
        return "TextField"

    def to_python(self, value):
        if value is None:
            return None
        elif value == "":
            return {}
        elif isinstance(value, basestring):
            try:
                return ast.literal_eval(value)
            except (ValueError, TypeError), e:
                print e
                raise exceptions.ValidationError(self.error_messages['invalid'] % value)
        
        if isinstance(value, dict):
            return value
        else:
            return {}
        
    def get_prep_value(self, value):
        if not value:
            return ""
        elif isinstance(value, basestring):
            return value
        else:
            return unicode(value)
            
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)
    
    def clean(self, value, model_instance):
        value = super(DictionaryField, self).clean(value, model_instance)
        return self.get_prep_value(value)
    
    def formfield(self, **kwargs):
        defaults = {'widget': forms.Textarea}
        defaults.update(kwargs)
        return super(DictionaryField, self).formfield(**defaults)
