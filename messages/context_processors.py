from messages.models import Message

def inbox(request):
    """Provide the count of unread messages for an authenticated user."""
    if request.user.is_authenticated():
        return {'messages_unread_count': Message.objects.inbox_unread_count(request.user)}
    else:
        return {}
