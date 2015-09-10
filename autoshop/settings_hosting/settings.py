"""
Django settings for sinkai project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mh8g5r$y8ighlew(1kq0ht-qanu%s^y_a0t9oizu0id^jmiko9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    'django.contrib.sitemaps',
    'robokassa',
    'ckeditor',
    'shop',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sinkai.urls'

WSGI_APPLICATION = 'sinkai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sinkaidb',
        'USER': 'sinkai',
        'PASSWORD': '2wsxXSW@',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/sinkai/sinkai/static'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)

MEDIA_URL = 'http://sinkai.it-national.com/media/'

#LOGIN SETTINGS
LOGIN_URL = '/login/'

# CKEDITOR SETTINGS
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# EMAIL BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'ns.it-national.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'testsite@it-national.com'
EMAIL_HOST_PASSWORD = '1qazZAQ!2'

# ROBOKASSA SETTINGS
ROBOKASSA_LOGIN = 'testsinkai'
ROBOKASSA_PASSWORD1 = 'test_sinkAi_1'
ROBOKASSA_PASSWORD2 = 'test_sinkAi_2'
ROBOKASSA_TEST_MODE = True # for test mode only
ROBOKASSA_STRICT_CHECK = True
ROBOKASSA_USE_POST = True
