import os

# Reference: https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl
# For handling the environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '68%jtx*w%(=gxshr&01gy@@*n!33ymhpuz+xf&lyk98$xlrge2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Our Apps
    'dashboard.apps.DashboardConfig',
    # Third Party - 1) All Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


'''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'joinus@joinourstory.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "nimadorostkar97@gmail.com"
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

# ------- for smtp ------
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nimadorostkar97@gmail.com'
EMAIL_HOST_PASSWORD = '--- your pass -----'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

'''

# Required for all-auth
SITE_ID = 1


# Provider specific settings for all-auth apps
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': str(os.getenv('FACEBOOK_CLIENT_ID')),
            'secret': str(os.getenv('FACEBOOK_SECRET_KEY')),
            'key': ''
        }
    },
    'google': {
        'APP': {
            'client_id': '820701086723-kllb69839qda9fjfhhrotnj0cmnnonvd.apps.googleusercontent.com',
            'secret': '4rbVyWPGfAxrGmFq98kzPFOp',
            'key': ''
        }
    },
    'twitter': {
        'APP': {
            'client_id': str(os.getenv('TWITTER_CLIENT_ID')),
            'secret': str(os.getenv('TWITTER_SECRET_KEY')),
            'key': ''
        }
    }
}





# Email Backend - Currently set at console/terminal
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Custom Settings - allauth
LOGIN_REDIRECT_URL = "/"




# Alphavantage key
ALPHAVANTAGE_KEY1 = str(os.getenv('ALPHAVANTAGE_KEY1'))
ALPHAVANTAGE_KEY2 = str(os.getenv('ALPHAVANTAGE_KEY2'))
ALPHAVANTAGE_KEY3 = str(os.getenv('ALPHAVANTAGE_KEY3'))
ALPHAVANTAGE_KEY4 = str(os.getenv('ALPHAVANTAGE_KEY4'))
ALPHAVANTAGE_KEY5 = str(os.getenv('ALPHAVANTAGE_KEY5'))
ALPHAVANTAGE_KEY6 = str(os.getenv('ALPHAVANTAGE_KEY6'))
ALPHAVANTAGE_KEY7 = str(os.getenv('ALPHAVANTAGE_KEY7'))
