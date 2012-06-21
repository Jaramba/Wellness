from django.template import Library
from userprofile.forms import RegistrationForm
from userprofile.countries import COUNTRIES
     
register = Library()
     
@register.filter
def country(country):
    for _country in COUNTRIES:
        if country in _country[0]:
            return _country[1]
    return "Not Set"

