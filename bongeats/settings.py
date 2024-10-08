"""
Django settings for bongeats project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from environ import Env

env = Env()
env.read_env()

ENVIRONMENT=env('ENVIRONMENT', default='production')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False


ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']



# Application definition
INSTALLED_APPS = [
    "daphne",
    "channels",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bongapp.apps.BongappConfig',
    'mathfilters',
    'fontawesome',
    'django_htmx',
    'django_celery_beat',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'bongeats.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#WSGI_APPLICATION = 'bongeats.wsgi.application'
ASGI_APPLICATION = 'bongeats.asgi.application'

# CHANNEL_LAYERS = {
#    "default": {
#        "BACKEND": "channels.layers.InMemoryChannelLayer"
#    }
# }
if DEBUG:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }
else:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [('redis://default:FzTIveiCBMkIeBsCMLWOPBScAfwzUDin@monorail.proxy.rlwy.net:20263')],
            },
        },
    }    
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [('redis://default:FzTIveiCBMkIeBsCMLWOPBScAfwzUDin@monorail.proxy.rlwy.net:20263')],
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.mail.yahoo.com' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#EMAIL_HOST_USER='rcdeep22@yahoo.com'
#EMAIL_HOST_PASSWORD = 'Debanjan22!'
EMAIL_HOST_USER = 'ridhimansin@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'qmod oilh eyef lsbg'  # Your Gmail password


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
   os.path.join(BASE_DIR / "static")
#'/var/www/static/',
]

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

STRIPE_PUBLIC_KEY = 'pk_test_51PjkGyP8vW4nFj074MLBrldxHjLcsmGoJCPyUL9aew81a1Ob59swiSMZdmcv1s1E7XJjo0toVYoRkKE6xj7QDnQ300fkn8MblW'
STRIPE_SECRET_KEY = 'sk_test_51PjkGyP8vW4nFj07CiFE4QR1ZG9vJ9cZljHQVm80XckO24Rwe0JrlnuwEDIOVit8jDl5P7D4eQMA4dmWPQB8qkgi00v4VxVw3x'
STRIPE_WEBHOOK_SECRET="whsec_65f6f35d4e47e750e587e997ff8d45c5a85cf516031e46f02dd0b8bc374efa2a"

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_RESULT_EXTENDED = True
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_USERNAME_BLACKLIST = ['admin', 'superuser', 'bongeats', 'bongeatsadmin', 'bongeatsuser', 'bongeatsadminuser','profile','login','logout','signup','register','password','reset','account','prof']