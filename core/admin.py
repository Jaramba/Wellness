from django.contrib import admin
from forms import *
from models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site

class CoreUserAdmin(UserAdmin):
    form = CoreUserChangeForm 
    
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'middle_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Groups'), {'fields': ('groups',)}),
    )
    
class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = [f.name for f in Person._meta.fields]
    inlines = []
admin.site.register(Person, PersonAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = [f.name for f in UserProfile._meta.fields]
    inlines = []
admin.site.register(UserProfile, UserProfileAdmin)

class AttachmentAdmin(admin.ModelAdmin):
    model = Attachment
    list_display = [f.name for f in Attachment._meta.fields]
admin.site.register(Attachment, AttachmentAdmin)    

class ReminderAdmin(admin.ModelAdmin):
    model = Reminder
    list_display = [f.name for f in Reminder._meta.fields]
admin.site.register(Reminder, ReminderAdmin)

admin.site.unregister(User)
admin.site.unregister(FlatPage)
admin.site.unregister(Comment)
admin.site.unregister(Site)
admin.site.register(User, CoreUserAdmin)