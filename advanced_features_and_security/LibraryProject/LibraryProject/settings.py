"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gx_u38@hl%!6^zsh$z_s4!3g+pc29+j3-b^1ghvqehcp&k)n8b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf.apps.BookshelfConfig',
    'relationship_app.apps.RelationshipAppConfig',
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

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = '/'  # or your preferred page after login

# Redirect to login page if not authenticated
LOGIN_URL = 'login'


AUTH_USER_MODEL = 'bookshelf.CustomUser'

SECURE_BROWSER_XSS_FILTER = True  # Enables the X-XSS-Protection header for XSS prevention
X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being embedded in iframes to prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents browsers from guessing the content type

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


MIDDLEWARE += ['csp.middleware.CSPMiddleware']

CSP_DEFAULT_SRC = ("'self'",)  # Only allow resources from this domain
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')  # Adjust as needed for stylesheets
CSP_SCRIPT_SRC = ("'self'", 'trusted-scripts.com')  # Add trusted script domains

SECURE_SSL_REDIRECT = True  # Redirects HTTP requests to HTTPS

SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Includes subdomains in the HSTS policy
SECURE_HSTS_PRELOAD = True  # Enables HSTS preloading in supported browsers

SESSION_COOKIE_SECURE = True  # Sends session cookies only over HTTPS
CSRF_COOKIE_SECURE = True  # Sends CSRF cookies only over HTTPS


X_FRAME_OPTIONS = 'DENY'  # Prevents embedding of your site in iframes
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents browsers from interpreting files as a different MIME type
SECURE_BROWSER_XSS_FILTER = True  # Enables XSS filtering in supported browsers
