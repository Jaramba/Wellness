from settings import _

SITE_NAME = 'WELLINGTON'
META_KEYWORDS = _('')
META_DESCRIPTION = _('')

# Cookie name. This can be whatever you want.
SESSION_COOKIE_NAME = 'sessionid'
# The module to store sessions data.
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 2
# Whether a user's session cookie expires when the Web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_SECURE = False

# e-mail settings
DEFAULT_FROM_EMAIL = 'noreply@wellington.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'inposting'
EMAIL_HOST_PASSWORD = 'a79fHH7722!'

#from util.mj_countries.models import Language
#LANGUAGES = Language.objects.filter(active=True)

DEFAULT_COMPANY_PACKAGE = 'starter package'
DEFAULT_USER_PACKAGE = 'starter package'
