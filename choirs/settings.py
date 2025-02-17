"""
Django settings for Choirs project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

from decouple import config
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool) == True
DEVELOPMENT_MODE = config("DEVELOPMENT_MODE", default=False, cast=bool) == True
# Allow accessing site at localhost:8000 during development
if DEVELOPMENT_MODE:
    ALLOWED_HOSTS = ["localhost"]
else:
    ALLOWED_HOSTS = [config("DOMAIN"), "www." + config("DOMAIN"), config("DOMAIN2"), "www." + config("DOMAIN2")]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    'django_sass',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'storages',

    # Local
    'users',
    'myAuth',
    'core',
    'songs',
    'groups',
    'events',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",

]

AUTH_USER_MODEL = "users.User"

ROOT_URLCONF = "choirs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                'django.template.context_processors.request',
                # Add the groups, events, and songs to every context (needed for navigation)
                'groups.context_processors.add_song_groups_to_all_views',
                'events.context_processors.add_events_to_all_views',
                'songs.context_processors.add_songs_to_all_views',
            ],
        },
    },
]

WSGI_APPLICATION = "choirs.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# if DEVELOPMENT_MODE is True:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": BASE_DIR / "db.sqlite3",
#         }
#     }
# else:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": "",
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Allauth settings
# Redirect to home URL after login (Default redirects to /accounts/profile/)
# This is hard coded, because reverse() is complaining that app isn't loaded yet
LOGIN_REDIRECT_URL = "/"
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

## Allauth email settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_EMAIL_NOTIFICATIONS = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

## Allauth email backend
if DEVELOPMENT_MODE:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_PORT")
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    DEFAULT_FROM_EMAIL = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = False
    EMAIL_USE_SSL = True
# allauth settings
# ACCOUNT_FORMS = {
#     "signup": "myAuth.forms.MyCustomSignupForm",
#     "change_password": "myAuth.forms.MyCustomChangePasswordForm",
#     "reset_password": "myAuth.forms.MyCustomResetPasswordForm",
# }

# recaptcha settings
# RECAPTCHA_PUBLIC_KEY = config("RECAPTCHA_PUBLIC_KEY")
# RECAPTCHA_PRIVATE_KEY = config("RECAPTCHA_PRIVATE_KEY")
# RECAPTCHA_DEFAULT_ACTION = "generic"
# RECAPTCHA_SCORE_THRESHOLD = 0.5
# RECAPTCHA_DOMAIN = config("DOMAIN")
# RECAPTCHA_URL = "https://www.google.com/recaptcha/api/siteverify"
# RECAPTCHA_TIMEOUT = 5



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "EST"

USE_I18N = True

USE_TZ = True


# AWS S3 for media storage
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = "public-read"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_S3_REGION_NAME = "us-east-2"
AWS_S3_SIGNATURE_VERSION = "s3v4"
DEFAULT_FILE_STORAGE = "choirs.storage_backends.MediaStorage"
# AWS S3 for media storage



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / "static/",)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
