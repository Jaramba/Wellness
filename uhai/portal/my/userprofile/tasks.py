from uhai.portal.api.sms.tasks import process_outgoingmessages
from django.contrib.auth.models import User

from models import SmsConfirmation

from celery.task.schedules import crontab  
from celery.decorators import periodic_task, task

@task
def confirm_sms(confirmation_key):
    try:
        confirmation = SmsConfirmation.objects.get(confirmation_key=confirmation_key)
    except SmsConfirmation.DoesNotExist:
        return None
    if not confirmation.key_expired():
        user = confirmation.user
        user.profile.verified = True
        user.profile.save()
        return confirmation

@periodic_task(run_every=crontab(hour="23"))
def delete_expired_confirmations():
    for confirmation in SmsConfirmation.objects.all():
        if confirmation.key_expired():
            confirmation.delete()

@task
def prepare_user_token(user_pk):
	user = User.objects.get(pk=user_pk)
	salt = sha_constructor(str(random())).hexdigest()[:5]
	confirmation_key = sha_constructor(salt + user.profile.mobile_phone).hexdigest()[:6]

	context = {
	    "user": mobile_phone.user,
	    "confirmation_key": confirmation_key,
	}
	message = ("Hello %(user)s, You have been enrolled "
	          "into Uhai, use %(confirmation_key)s "
	          "to log on to http://www.uhai.co.ke/register") % context           
	process_outgoingmessages.delay(message, mobile_phone.user.pk)
	return SmsConfirmation.objects.create(
	    user=user,
	    sent=datetime.now(),
	    confirmation_key=confirmation_key)
