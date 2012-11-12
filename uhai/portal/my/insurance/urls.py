from django.conf.urls.defaults import *

from app_map import VIEW_NAME, APP_MAP

from uhai.core.funcs import get_crud_urls

urlpatterns = get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP
)