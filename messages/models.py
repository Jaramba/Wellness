import hashlib

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import truncate_words
from django.utils.translation import ugettext, ugettext_lazy as _
try:
    from django.utils.timezone import now   # Django 1.4 aware datetimes
except ImportError:
    from datetime import datetime
    now = datetime.now

from messages.urls import OPTION_MESSAGES
from messages.utils import email_visitor, notify_user

# moderation constants
STATUS_PENDING = 'p'
STATUS_ACCEPTED = 'a'
STATUS_REJECTED = 'r'
STATUS_CHOICES = (
    (STATUS_PENDING, _('Pending')),
    (STATUS_ACCEPTED, _('Accepted')),
    (STATUS_REJECTED, _('Rejected')),
)
# ordering constants
ORDER_BY_KEY = 'o' # as 'order'
ORDER_BY_FIELDS = {
    'f': 'sender__username',    # as 'from'
    't': 'recipient__username', # as 'to'
    's': 'subject',  # as 'subject'
    'd': 'sent_at',  # as 'date'
}
ORDER_BY_MAPPER = {'sender': 'f', 'recipient': 't', 'subject': 's', 'date': 'd'} # for templatetags usage

dbms = settings.DATABASES['default']['ENGINE'].rsplit('.',1)[-1]
QUOTE_CHAR = '`' if dbms == 'mysql' else '"'

def get_order_by(query_dict):
    """
    Return a field name, optionally prefixed for descending order, or None if not found.

    Argument:
    ``query_dict``: a dictionary to look for a key dedicated to ordering purpose

    >>> get_order_by({})
    
    >>> get_order_by({ORDER_BY_KEY: 'f'})
    'sender__username'
    >>> get_order_by({ORDER_BY_KEY: 'D'})
    '-sent_at'
    """
    if ORDER_BY_KEY in query_dict:
        code = query_dict[ORDER_BY_KEY] # code may be uppercase or lowercase
        order_by_field = ORDER_BY_FIELDS.get(code.lower())
        if order_by_field:
            if code.isupper():
                order_by_field = '-' + order_by_field
            return order_by_field

class MessageManager(models.Manager):
    """The manager for Message."""

    @property
    def _last_in_thread(self):
        """Return the latest message id for each conversation."""
        return self.filter(thread__isnull=False).values('thread').annotate(models.Max('pk'))\
            .values_list('pk__max', flat=True).order_by()

    def _folder(self, related, filters, option=None, order_by=None):
        """Base code, in common to the folders."""
        if related:
            qs = self.select_related(*related)
        else:
            qs = self.all()
        if order_by:
            qs = qs.order_by(order_by)
        if isinstance(filters, (list,tuple)):
            lookups = models.Q()
            for filter in filters:
                lookups |= models.Q(**filter)
        else:
            lookups = models.Q(**filters)
        if option == OPTION_MESSAGES:
            return qs.filter(lookups)
            # Adding a 'count' attribute, to be similar to the by-conversation case,
            # should not be necessary. Otherwise add:
            # .extra(select={'count': 'SELECT 1'})
        else:
            return qs.filter(
                models.Q(id__in=self._last_in_thread.filter(lookups)) | models.Q(lookups, thread__isnull=True)
            ).extra(select={'count': QUOTE_CHAR.join([
            'SELECT COUNT(*) FROM ', 'messages_message', ' T'
            ' WHERE T.', 'thread_id', ' = ', 'messages_message', '.', 'thread_id', ' '
            ])})
            # For single message, 'count' is returned as 0. Should be acceptable if known.
            # If not, replace "COUNT(*)" by "1+COUNT(*)" and add:
            # ' AND T."id" <> T."thread_id"'

    def inbox(self, user, related=True, **kwargs):
        """
        Return accepted messages received by a user but not marked as archived or deleted.
        """
        related = ('sender',) if related else None
        filters = {
            'recipient': user,
            'recipient_archived': False,
            'recipient_deleted_at__isnull': True,
            'moderation_status': STATUS_ACCEPTED,
        }
        return self._folder(related, filters, **kwargs)

    def inbox_unread_count(self, user):
        """
        Return the number of unread messages for a user.

        Designed for context_processors.py and templatetags/messages_tags.py

        """
        return self.inbox(user, related=False, option=OPTION_MESSAGES).filter(read_at__isnull=True).count()
    
    def sent(self, user, **kwargs):
        """
        Return all messages sent by a user but not marked as archived or deleted.
        """
        related = ('recipient',)
        filters = {
            'sender': user,
            'sender_archived': False,
            'sender_deleted_at__isnull': True,
            # allow to see pending and rejected messages as well
        }
        return self._folder(related, filters, **kwargs)

    def archives(self, user, **kwargs):
        """
        Return messages belonging to a user and marked as archived.
        """
        related = ('sender','recipient')
        filters = ({
            'recipient': user,
            'recipient_archived': True,
            'recipient_deleted_at__isnull': True,
            'moderation_status': STATUS_ACCEPTED,
        }, {
            'sender': user,
            'sender_archived': True,
            'sender_deleted_at__isnull': True,
        })
        return self._folder(related, filters, **kwargs)

    def trash(self, user, **kwargs):
        """
        Return messages belonging to a user and marked as deleted.
        """
        related = ('sender','recipient')
        filters = ({
            'recipient': user,
            'recipient_deleted_at__isnull': False,
            'moderation_status': STATUS_ACCEPTED,
        }, {
            'sender': user,
            'sender_deleted_at__isnull': False,
        })
        return self._folder(related, filters, **kwargs)

    def thread(self, user, filter):
        """
        Return message/conversation for display.
        """
        return self.select_related('sender','recipient').filter(
            filter,
            (models.Q(recipient=user) & models.Q(moderation_status=STATUS_ACCEPTED)) | models.Q(sender=user),
        ).order_by('sent_at')

    def perms(self, user):
        """
        Return a field-lookups filter as a permission controller for a reply request.

        The user must be the recipient of the accepted, non-deleted, message

        """
        return models.Q(recipient=user) & models.Q(moderation_status=STATUS_ACCEPTED) & models.Q(recipient_deleted_at__isnull=True)

    def set_read(self, user, filter):
        """
        Set messages as read.
        """
        return self.filter(
            filter,
            recipient=user,
            moderation_status=STATUS_ACCEPTED,
            read_at__isnull=True,
        ).update(read_at=now())

class Message(models.Model):
    """
    A message between a User and another User or an AnonymousUser.
    """

    SUBJECT_MAX_LENGTH = 120

    subject = models.CharField(_("subject"), max_length=SUBJECT_MAX_LENGTH)
    body = models.TextField(_("body"), blank=True)
    sender = models.ForeignKey(User, related_name='sent_messages', null=True, blank=True, verbose_name=_("sender"))
    recipient = models.ForeignKey(User, related_name='received_messages', null=True, blank=True, verbose_name=_("recipient"))
    email = models.EmailField(_("visitor"), blank=True) # instead of either sender or recipient, for an AnonymousUser
    parent = models.ForeignKey('self', related_name='next_messages', null=True, blank=True, verbose_name=_("parent message"))
    thread = models.ForeignKey('self', related_name='child_messages', null=True, blank=True, verbose_name=_("root message"))
    sent_at = models.DateTimeField(_("sent at"), default=now)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)
    replied_at = models.DateTimeField(_("replied at"), null=True, blank=True)
    sender_archived = models.BooleanField(_("archived by sender"))
    recipient_archived = models.BooleanField(_("archived by recipient"))
    sender_deleted_at = models.DateTimeField(_("deleted by sender at"), null=True, blank=True)
    recipient_deleted_at = models.DateTimeField(_("deleted by recipient at"), null=True, blank=True)
    # moderation fields
    moderation_status = models.CharField(_("status"), max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
    moderation_by = models.ForeignKey(User, related_name='moderated_messages',
        null=True, blank=True, verbose_name=_("moderator"))
    moderation_date = models.DateTimeField(_("moderated at"), null=True, blank=True)
    moderation_reason = models.CharField(_("rejection reason"), max_length=120, blank=True)

    objects = MessageManager()

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")
        ordering = ['-sent_at', '-id']

    def __unicode__(self):
        return u"{0}>{1}:{2}".format(self.obfuscated_sender, self.obfuscated_recipient, truncate_words(self.subject,5))

    @models.permalink
    def get_absolute_url(self):
        return ('messages_view', [str(self.pk)])

    def is_pending(self):
        """Tell if the message is in the pending state."""
        return self.moderation_status == STATUS_PENDING
    def is_rejected(self):
        """Tell if the message is in the rejected state."""
        return self.moderation_status == STATUS_REJECTED
    def is_accepted(self):
        """Tell if the message is in the accepted state."""
        return self.moderation_status == STATUS_ACCEPTED

    @property
    def is_new(self):
        """Tell if the recipient has not yet read the message."""
        return self.read_at is None

    @property
    def is_replied(self):
        """Tell if the recipient has written a reply to the message."""
        return self.replied_at is not None

    def _obfuscated_email(self):
        """
        Return the email field as obfuscated, to keep it undisclosed.

        Format is:
            first 4 characters of the hash email + '..' + last 4 characters of the hash email + '@' + domain without TLD
        Example:
            foo@domain.com -> 1a2b..e8f9@domain

        """
        email = self.email
        digest = hashlib.md5(email + settings.SECRET_KEY).hexdigest()
        shrunken_digest = '..'.join((digest[:4], digest[-4:])) # 32 characters is too long and is useless
        bits = email.split('@')
        if len(bits) <> 2:
            return u''
        domain = bits[1]
        return '@'.join((shrunken_digest, domain.rsplit('.',1)[0])) # leave off the TLD to gain some space

    def admin_sender(self):
        """
        Return the sender either as a username or as a plain email.
        Designed for the Admin site.

        """
        if self.sender:
            return str(self.sender)
        else:
            return '<{0}>'.format(self.email)
    admin_sender.short_description = _("sender")
    admin_sender.admin_order_field = 'sender'

    # Give the sender either as a username or as a plain email.
    clear_sender = property(admin_sender)

    @property
    def obfuscated_sender(self):
        """Return the sender either as a username or as an undisclosed email."""
        if self.sender:
            return unicode(self.sender)
        else:
            return self._obfuscated_email()

    def admin_recipient(self):
        """
        Return the recipient either as a username or as a plain email.
        Designed for the Admin site.

        """
        if self.recipient:
            return str(self.recipient)
        else:
            return '<{0}>'.format(self.email)
    admin_recipient.short_description = _("recipient")
    admin_recipient.admin_order_field = 'recipient'

    # Give the recipient either as a username or as a plain email.
    clear_recipient = property(admin_recipient)

    @property
    def obfuscated_recipient(self):
        """Return the recipient either as a username or as an undisclosed email."""
        if self.recipient:
            return unicode(self.recipient)
        else:
            return self._obfuscated_email()

    def get_replies_count(self):
        """Return the number of accepted responses."""
        return self.next_messages.filter(moderation_status=STATUS_ACCEPTED).count()

    def quote(self, format_subject, format_body):
        """Return a dictionary of quote values to initiate a reply."""
        return {
            'subject': format_subject(self.subject)[:self.SUBJECT_MAX_LENGTH],
            'body': format_body(self.obfuscated_sender, self.body),
        }

    def clean(self):
        """Check some validity constraints."""
        if not (self.sender_id or self.email):
            raise ValidationError(ugettext("Undefined sender."))

    def clean_moderation(self, initial_status, user=None):
        """Adjust automatically some fields, according to status workflow."""
        if self.moderation_status <> initial_status:
            self.moderation_date = now()
            self.moderation_by = user
            if self.is_rejected():
                # even if maybe previously deleted during a temporary 'accepted' stay
                self.recipient_deleted_at = now()
            elif initial_status == STATUS_REJECTED:
                # rollback
                self.recipient_deleted_at = None

    def clean_for_visitor(self):
        """Do some auto-read and auto-delete, because there is no one to do it (no account)."""
        if not self.sender_id:
            # no need to wait for a final moderation status to mark as deleted
            if not self.sender_deleted_at:
                self.sender_deleted_at = now()
        elif not self.recipient_id:
            if self.is_accepted():
                if not self.read_at:
                    self.read_at = now()
                if not self.recipient_deleted_at:
                    self.recipient_deleted_at = now()
            else:
                # rollbacks
                if self.read_at:
                    self.read_at = None
                # but stay deleted if rejected
                if self.is_pending() and self.recipient_deleted_at:
                    self.recipient_deleted_at = None

    def update_parent(self, initial_status):
        """Update the parent to actualize its response state."""
        if self.moderation_status <> initial_status:
            parent = self.parent
            if self.is_accepted():
                # keep the very first date; no need to do differently
                if parent and (not parent.replied_at or self.sent_at < parent.replied_at):
                    parent.replied_at = self.sent_at
                    parent.save()
            elif initial_status == STATUS_ACCEPTED:
                if parent and parent.replied_at == self.sent_at:
                    # rollback, but there may be some other valid replies
                    try:
                        other_date = parent.next_messages\
                            .exclude(pk=self.pk).filter(moderation_status=STATUS_ACCEPTED)\
                            .values_list('sent_at', flat=True)\
                            .order_by('sent_at')[:1].get()
                        parent.replied_at = other_date
                    except Message.DoesNotExist:
                        parent.replied_at = None
                    parent.save()

    def notify_users(self, initial_status, is_auto_moderated=True):
        """Notify the rejection (to sender) or the acceptance (to recipient) of the message."""
        if initial_status == STATUS_PENDING:
            if self.is_rejected():
                # Bypass: for an online user, no need to notify when rejection is immediate.
                # Only useful for a visitor as an archive copy of the message, otherwise lost.
                if not (self.sender_id and is_auto_moderated):
                    (notify_user if self.sender_id else email_visitor)(self, 'rejection')
            elif self.is_accepted():
                (notify_user if self.recipient_id else email_visitor)(self, 'acceptance')

    def get_dates(self):
        """Get some dates to restore later."""
        return (self.sender_deleted_at, self.recipient_deleted_at, self.read_at)

    def set_dates(self, sender_deleted_at, recipient_deleted_at, read_at):
        """Restore some dates."""
        self.sender_deleted_at = sender_deleted_at
        self.recipient_deleted_at = recipient_deleted_at
        self.read_at = read_at

    def get_moderation(self):
        """Get moderation information to restore later."""
        return (self.moderation_status, self.moderation_by_id, self.moderation_date, self.moderation_reason)

    def set_moderation(self, status, by_id, date, reason):
        """Restore moderation information."""
        self.moderation_status = status
        self.moderation_by_id = by_id
        self.moderation_date = date
        self.moderation_reason = reason

    def auto_moderate(self, moderators):
        """Run a chain of auto-moderators."""
        auto = None
        final_reason = ''
        percents = []
        reasons = []
        if not isinstance(moderators, (list, tuple)):
            moderators = (moderators,)
        for moderator in moderators:
            rating = moderator(self)
            if rating is None: continue
            if isinstance(rating, tuple):
                percent, reason = rating
            else:
                percent = rating
                reason = getattr(moderator, 'default_reason', '')
            if percent is False: percent = 0
            if percent is True: percent = 100
            if not 0 <= percent <= 100: continue
            if percent == 0:
                auto = False
                final_reason = reason
                break
            elif percent == 100:
                auto = True
                break
            percents.append(percent)
            reasons.append(reason)
        if auto is None and percents:
            average = float(sum(percents)) / len(percents)
            final_reason = ', '.join([r for i,r in enumerate(reasons) if r and not r.isspace() and percents[i] < 50])
            auto = average >= 50
        if auto is None:
            auto = getattr(settings, 'messages_AUTO_MODERATE_AS', None)
        if auto is True:
            self.moderation_status = STATUS_ACCEPTED
        elif auto is False:
            self.moderation_status = STATUS_REJECTED
            self.moderation_reason = final_reason

class PendingMessageManager(models.Manager):
    """The manager for PendingMessage."""

    def get_query_set(self):
        """Filter to get only pending objects."""
        return super(PendingMessageManager, self).get_query_set().filter(moderation_status=STATUS_PENDING)

class PendingMessage(Message):
    """
    A proxy to Message, focused on pending objects to accept or reject.
    """

    objects = PendingMessageManager()

    class Meta:
        verbose_name = _("pending message")
        verbose_name_plural = _("pending messages")
        proxy = True

    def set_accepted(self):
        """Set the message as accepted."""
        self.moderation_status = STATUS_ACCEPTED

    def set_rejected(self):
        """Set the message as rejected."""
        self.moderation_status = STATUS_REJECTED
