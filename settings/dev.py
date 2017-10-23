from base import *

DEBUG = True
 
INSTALLED_APPS.append('debug_toolbar')
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe Environment Variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_AvpCDlvstfiG8aJg04QKhIS4')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_h7nJ6fMm169xVpqizlmtnvni')


'debug_toolbar.middleware.DebugToolbarMiddleware',


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]