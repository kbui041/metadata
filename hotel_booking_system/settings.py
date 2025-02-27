"""
Django settings for hotel_booking_system project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y&1z3hqbxwnz#h5y@-tisrg9#d3ao$ddvqg9q@z=)!i!(1(885'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allowed hosts for the application
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin
    'django.contrib.auth',  # Django authentication
    'django.contrib.contenttypes',  # Django content types
    'django.contrib.sessions',  # Django sessions
    'django.contrib.messages',  # Django messages
    'django.contrib.staticfiles',  # Django static files
    'django_filters',  # Django filters
    'bookings',  # Bookings application
    'rest_framework',  # Django REST framework
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
    'hotel_booking_system.middleware.FaviconMiddleware',  # Custom favicon middleware
    'hotel_booking_system.middleware.LoggingMiddleware',  # Custom logging middleware
    #'hotel_booking_system.middleware.JWTAuthenticationMiddleware',  # Custom JWT authentication middleware
    'hotel_booking_system.middleware.JsonResponseMiddleware',  # Custom JSON response middleware
]

# Root URL configuration
ROOT_URLCONF = 'hotel_booking_system.urls'

# settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template backend
        'DIRS': [],  # Directories for templates
        'APP_DIRS': True,  # Enable auto-loading of templates from installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug context processor
                'django.template.context_processors.request',  # Request context processor
                'django.contrib.auth.context_processors.auth',  # Authentication context processor
                'django.contrib.messages.context_processors.messages',  # Message context processor
            ],
        },
    },
]

# WSGI application configuration
WSGI_APPLICATION = 'hotel_booking_system.wsgi.application'

# Database configuration
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Database name
    }
}

# settings.py

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Similarity validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum length validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Common password validator
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Numeric password validator
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'  # Default language code

TIME_ZONE = 'UTC'  # Default time zone

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable time zone support

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'  # URL to use for static files

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default auto field type
