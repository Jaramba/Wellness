import sys

from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _

name = getattr(settings, 'messages_NOTIFIER_APP', 'notification')
if name and name in settings.INSTALLED_APPS:
    name = name + '.models'
    __import__(name)
    notification = sys.modules[name]

    def create_notice_types(*args, **kwargs):
        notification.create_notice_type("messages_rejection", _("Message Rejected"), _("Your message has been rejected"))
        notification.create_notice_type("messages_message", _("Message Received"), _("You have received a message"))
        notification.create_notice_type("messages_reply", _("Reply Received"), _("You have received a reply"))

    signals.post_syncdb.connect(create_notice_types, sender=notification)

