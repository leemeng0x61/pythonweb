"""
Django settings for mysite project.

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
SECRET_KEY = '9zjeoy=$dpe(+6*kc!%wr*uae$45_u$3zp)-*!qxazq$_o#r(p'

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
    'django.contrib.sites',
#     'bootstrap3',
    'd'
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

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#              
#     'product': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.  
        'NAME': 'test',   
        'USER': 'root',                      # Not used with sqlite3.  
        'PASSWORD': 'root',                  # Not used with sqlite3.  
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.  
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.  
    }  

}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1

# # Default settings
# BOOTSTRAP3 = {
# 
#     # The URL to the jQuery JavaScript file
#     'jquery_url': '//code.jquery.com/jquery.min.js',
# 
#     # The Bootstrap base URL
#     'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.3.1/',
# 
#     # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
#     'css_url': None,
# 
#     # The complete URL to the Bootstrap CSS file (None means no theme)
#     'theme_url': None,
# 
#     # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
#     'javascript_url': None,
# 
#     # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
#     'javascript_in_head': False,
# 
#     # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
#     'include_jquery': False,
# 
#     # Label class to use in horizontal forms
#     'horizontal_label_class': 'col-md-2',
# 
#     # Field class to use in horizontal forms
#     'horizontal_field_class': 'col-md-4',
# 
#     # Set HTML required attribute on required fields
#     'set_required': True,
# 
#     # Set placeholder attributes to label if no placeholder is provided
#     'set_placeholder': True,
# 
#     # Class to indicate required (better to set this in your Django form)
#     'required_css_class': '',
# 
#     # Class to indicate error (better to set this in your Django form)
#     'error_css_class': 'has-error',
# 
#     # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
#     'success_css_class': 'has-success',
# 
#     # Renderers (only set these if you have studied the source and understand the inner workings)
#     'formset_renderers':{
#         'default': 'bootstrap3.renderers.FormsetRenderer',
#     },
#     'form_renderers': {
#         'default': 'bootstrap3.renderers.FormRenderer',
#     },
#     'field_renderers': {
#         'default': 'bootstrap3.renderers.FieldRenderer',
#         'inline': 'bootstrap3.renderers.InlineFieldRenderer',
#     },
# }