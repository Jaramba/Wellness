from django.conf.urls.defaults import *

from app_map import VIEW_NAME, APP_MAP
from uhai.core.utils import get_crud_urls

from django.views.generic.base import TemplateView

from forms_builder.forms.models import Form

urlpatterns = patterns(VIEW_NAME,
    url(r'^$', 'index', name='programs'),
	url(r'^questionaires/$', lambda request: TemplateView.as_view(
        template_name="programs/questionnaire_list.html")(request, forms=Form.objects.all()), 
		name="questionnaire-list"),
	url(r'^forms/', include('forms_builder.forms.urls')),
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP
)
