"""
Written as in contrib/admin/templatetags/admin_modify.py,
to define a customized version of 'submit_row' tag with a cutomized html template.

In use in templates/admin/messages/pendingmessage/change_form.html.
"""
from django import template

register = template.Library()

@register.inclusion_tag('admin/messages/pendingmessage/submit_line.html')
def messages_submit_row():
    return {}
