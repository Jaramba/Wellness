"""
URLconf for tests.py usage.

"""
from django.conf import settings
try:
    from django.conf.urls import patterns, include, url # django 1.4
except ImportError:
    from django.conf.urls.defaults import patterns, include, url # django 1.3
from django.forms import ValidationError
from django.views.generic.simple import redirect_to

from messages.urls import OPTIONS

# user_filter function set
def user_filter_reason(user):
    if user.username == 'bar': return 'some reason'
    return None
def user_filter_no_reason(user):
    return ''
def user_filter_false(user):
    return False
def user_filter_exception(user):
    if user.username == 'bar': raise ValidationError(['first good reason',"anyway, I don't like {0}".format(user.username)])
    return None

# exchange_filter function set
def exch_filter_reason(sender, recipient, recipients_list):
    if recipient.username=='bar': return 'some reason'
    return None
def exch_filter_no_reason(sender, recipient, recipients_list):
    return ''
def exch_filter_false(sender, recipient, recipients_list):
    return False
def exch_filter_exception(sender, recipient, recipients_list):
    if recipient.username == 'bar': raise ValidationError(['first good reason',"anyway, I don't like {0}".format(recipient.username)])
    return None

# auto-moderation function set
def moderate_as_51(message):
    return 51
def moderate_as_48(message):
    return (48, "some reason")
moderate_as_48.default_reason = 'some default reason'

# quote formatters
def format_subject(subject):
    return "Re_ " + subject
def format_body(sender, body):
    return "{0} _ {1}".format(sender, body)

messages_patterns = patterns('messages.views',
    # Basic set
    url(r'^inbox/(?:(?P<option>'+OPTIONS+')/)?$', 'inbox', name='messages_inbox'),
    url(r'^sent/(?:(?P<option>'+OPTIONS+')/)?$', 'sent', name='messages_sent'),
    url(r'^archives/(?:(?P<option>'+OPTIONS+')/)?$', 'archives', name='messages_archives'),
    url(r'^trash/(?:(?P<option>'+OPTIONS+')/)?$', 'trash', name='messages_trash'),
    url(r'^write/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', name='messages_write'),
    url(r'^reply/(?P<message_id>[\d]+)/$', 'reply', name='messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', 'view', name='messages_view'),
    url(r'^view/t/(?P<thread_id>[\d]+)/$', 'view_conversation', name='messages_view_conversation'),
    url(r'^archive/$', 'archive', name='messages_archive'),
    url(r'^delete/$', 'delete', name='messages_delete'),
    url(r'^undelete/$', 'undelete', name='messages_undelete'),
    (r'^$', redirect_to, {'url': 'inbox/'}),

    # Customized set
    # 'success_url'
    url(r'^write_sent/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'success_url': 'messages_sent'}, name='messages_write_with_success_url_to_sent'),
    url(r'^reply_sent/(?P<message_id>[\d]+)/$', 'reply', {'success_url': 'messages_sent'}, name='messages_reply_with_success_url_to_sent'),
    url(r'^archive_arch/$', 'archive', {'success_url': 'messages_archives'}, name='messages_archive_with_success_url_to_archives'),
    url(r'^delete_arch/$', 'delete', {'success_url': 'messages_archives'}, name='messages_delete_with_success_url_to_archives'),
    url(r'^undelete_arch/$', 'undelete', {'success_url': 'messages_archives'}, name='messages_undelete_with_success_url_to_archives'),
    # 'max'
    url(r'^write_max/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'max': 1}, name='messages_write_with_max'),
    url(r'^reply_max/(?P<message_id>[\d]+)/$', 'reply', {'max': 1}, name='messages_reply_with_max'),
    # 'user_filter' on write
    url(r'^write_user_filter_reason/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'user_filter': user_filter_reason}, name='messages_write_with_user_filter_reason'),
    url(r'^write_user_filter_no_reason/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'user_filter': user_filter_no_reason}, name='messages_write_with_user_filter_no_reason'),
    url(r'^write_user_filter_false/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'user_filter': user_filter_false}, name='messages_write_with_user_filter_false'),
    url(r'^write_user_filter_exception/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'user_filter': user_filter_exception}, name='messages_write_with_user_filter_exception'),
    # 'user_filter' on reply
    url(r'^reply_user_filter_reason/(?P<message_id>[\d]+)/$', 'reply', {'user_filter': user_filter_reason}, name='messages_reply_with_user_filter_reason'),
    url(r'^reply_user_filter_no_reason/(?P<message_id>[\d]+)/$', 'reply', {'user_filter': user_filter_no_reason}, name='messages_reply_with_user_filter_no_reason'),
    url(r'^reply_user_filter_false/(?P<message_id>[\d]+)/$', 'reply', {'user_filter': user_filter_false}, name='messages_reply_with_user_filter_false'),
    url(r'^reply_user_filter_exception/(?P<message_id>[\d]+)/$', 'reply', {'user_filter': user_filter_exception}, name='messages_reply_with_user_filter_exception'),
    # 'exchange_filter' on write
    url(r'^write_exch_filter_reason/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'exchange_filter': exch_filter_reason}, name='messages_write_with_exch_filter_reason'),
    url(r'^write_exch_filter_no_reason/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'exchange_filter': exch_filter_no_reason}, name='messages_write_with_exch_filter_no_reason'),
    url(r'^write_exch_filter_false/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'exchange_filter': exch_filter_false}, name='messages_write_with_exch_filter_false'),
    url(r'^write_exch_filter_exception/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'exchange_filter': exch_filter_exception}, name='messages_write_with_exch_filter_exception'),
    # 'exchange_filter' on reply
    url(r'^reply_exch_filter_reason/(?P<message_id>[\d]+)/$', 'reply', {'exchange_filter': exch_filter_reason}, name='messages_reply_with_exch_filter_reason'),
    url(r'^reply_exch_filter_no_reason/(?P<message_id>[\d]+)/$', 'reply', {'exchange_filter': exch_filter_no_reason}, name='messages_reply_with_exch_filter_no_reason'),
    url(r'^reply_exch_filter_false/(?P<message_id>[\d]+)/$', 'reply', {'exchange_filter': exch_filter_false}, name='messages_reply_with_exch_filter_false'),
    url(r'^reply_exch_filter_exception/(?P<message_id>[\d]+)/$', 'reply', {'exchange_filter': exch_filter_exception}, name='messages_reply_with_exch_filter_exception'),
    # 'auto_moderators'
    url(r'^write_moderate/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'auto_moderators': (moderate_as_51,moderate_as_48)}, name='messages_write_moderate'),
    url(r'^reply_moderate/(?P<message_id>[\d]+)/$', 'reply', {'auto_moderators': (moderate_as_51,moderate_as_48)}, name='messages_reply_moderate'),
    # 'formatters'
    url(r'^reply_formatters/(?P<message_id>[\d]+)/$', 'reply', {'formatters': (format_subject,format_body)}, name='messages_reply_formatters'),
    url(r'^view_formatters/(?P<message_id>[\d]+)/$', 'view', {'formatters': (format_subject,format_body)}, name='messages_view_formatters'),
    # auto-complete
    url(r'^write_ac/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'autocomplete_channels': ('messages_multiple', None)}, name='messages_write_auto_complete'),
    url(r'^reply_ac/(?P<message_id>[\d]+)/$', 'reply', {'autocomplete_channel': 'messages_multiple'}, name='messages_reply_auto_complete'),
    # 'template_name'
    url(r'^inbox_template/(?:(?P<option>'+OPTIONS+')/)?$', 'inbox', {'template_name': 'messages/fake.html'}, name='messages_inbox_template'),
    url(r'^sent_template/(?:(?P<option>'+OPTIONS+')/)?$', 'sent', {'template_name': 'messages/fake.html'}, name='messages_sent_template'),
    url(r'^archives_template/(?:(?P<option>'+OPTIONS+')/)?$', 'archives', {'template_name': 'messages/fake.html'}, name='messages_archives_template'),
    url(r'^trash_template/(?:(?P<option>'+OPTIONS+')/)?$', 'trash', {'template_name': 'messages/fake.html'}, name='messages_trash_template'),
    url(r'^write_template/(?:(?P<recipients>[\w.@+-:]+)/)?$', 'write', {'template_name': 'messages/fake.html'}, name='messages_write_template'),
    url(r'^reply_template/(?P<message_id>[\d]+)/$', 'reply', {'template_name': 'messages/fake.html'}, name='messages_reply_template'),
    url(r'^view_template/(?P<message_id>[\d]+)/$', 'view', {'template_name': 'messages/fake.html'}, name='messages_view_template'),
    url(r'^view_template/t/(?P<thread_id>[\d]+)/$', 'view_conversation', {'template_name': 'messages/fake.html'}, name='messages_view_conversation_template'),
)

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'), # because of the login_required decorator
    (r'^messages/', include(messages_patterns)),
)

# because of fields.py/AutoCompleteWidget/render()/reverse()
if 'ajax_select' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^ajax_select/', include('ajax_select.urls')), # django-ajax-selects
    )

# optional
if 'notification' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^notification/', include('notification.urls')), # django-notification
    )
