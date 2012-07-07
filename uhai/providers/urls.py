from django.conf.urls.defaults import *

from app_map import MODULE_NAME, APP_MAP

from uhai.core.utils import get_crud_urls

urlpatterns = get_crud_urls(
    MODULE_NAME,
	app_map=APP_MAP
)
