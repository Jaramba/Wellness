from django.contrib import admin
from core.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    
    list_display = [f.name for f in UserProfile._meta.fields]
    list_filter = [f.name for f in UserProfile._meta.fields if f.name not in ('user','id','phone','postal_address', 'cv')]
    list_per_page = 25
    ordering = ('date_created',)
    search_fields = list_display

admin.site.register(UserProfile, UserProfileAdmin)