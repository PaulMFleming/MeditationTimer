from base import *

DEBUG = False


# Stripe Environment Variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_AvpCDlvstfiG8aJg04QKhIS4')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_h7nJ6fMm169xVpqizlmtnvni')


SITE_URL = 'https://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}