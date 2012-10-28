from django.contrib.auth.models import Group
from django.conf import settings
def request(request):	
    return {
    	'STAGE': settings.STAGE
    }