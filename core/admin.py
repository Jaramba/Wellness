from django.contrib import admin
from forms import *
from models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site

class UserProfileAdmin(admin.StackedInline):
    template = 'admin/edit_inline/single_stacked.html'
    model = UserProfile
    extra = 1

class UserUserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (('Groups'), {'fields': ('groups',)}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    #OK, I tried @staticmethod, didnt work, weirdly, this works
    def first_name(self):
        return self.profile.first_name or ''
    def middle_name(self, user):
        return user.profile.middle_name or ''
    def last_name(self):
        return self.profile.last_name or ''
    def mobile_phone(self, user):
        return user.profile.mobile_phone or ''
    
    list_display = ('username', 'email', first_name, 'middle_name', last_name, 'mobile_phone', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    inlines = (UserProfileAdmin,)

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = [f.name for f in Person._meta.fields if f.name not in [
          'photo', 
          'country', 
          'nationality', 
          'id', 
          'date_created', 
          'date_edited'
          ]
    ]
    inlines = []
    
    def queryset(self, request):
        qs = super(PersonAdmin, self).queryset(request)
        return qs.filter(userprofile__isnull=True)
    
admin.site.register(Person, PersonAdmin)

class AttachmentAdmin(admin.ModelAdmin):
    model = Attachment
    list_display = [f.name for f in Attachment._meta.fields]
admin.site.register(Attachment, AttachmentAdmin)    

admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.register(User, UserUserProfileAdmin)
admin.site.register(Relationship)
admin.site.register(RelationshipType)