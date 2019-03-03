"""
Django settings for OkRellBackend project.

Using django version 2.1.7
"""

import os
# The main directory where the actual project is stored. 
# Ensure that only BASE_DIR is used to reference a file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8h^esg9ha)f^i)lz_*@$#z8rjl(rq-jv&$m9i^#g9au5v=!h3z'

# Turn Debug mode on before even starting to develop 
# Simply set this value DEBUG to True
# If a single migration is even detected to the production server. "YOU'RE FIRED"
DEBUG = True

# Add allowed host to this list on deployment
ALLOWED_HOSTS = ['okrella']


# Application definition
# If you are adding new apps then putthem in here
# Rules to add a new app
# format this string to fit your app name  --> {app}.apps.{app}Config
# Don't add apps using just the apps name. Inconsistent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main.apps.MainConfig',
    'Management.apps.ManagementConfig',
]

# Don't make any changes to this before talking to me. DIRECTLY
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# This is the the root url module that will be handling url direction
ROOT_URLCONF = 'OkRellBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add more items to list if you're adding static html templates to an app
        # We strictly enforce use of only the prespecified front-end technology
        'DIRS': [os.path.join(BASE_DIR, 'okrellfrontend/dist')],
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

# DON'T EVEN DARE
WSGI_APPLICATION = 'OkRellBackend.wsgi.application'


# This is the database config. In future we shall be using two different databases.
# One for testing and one for development, With similar schema but not even close to the amount of data they hold 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcau5uv06inhmh',
        'USER': 'yhzkqexduihimr',
        'PASSWORD': '172cfd4109ee47a1def27c0e0daf9fcbb44e81611822fc7bdc7a8c01dbce174a',
        'HOST': 'ec2-54-83-17-151.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Make changes to this test database variable if we decide to change the test database engine
if DEBUG:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testokrell',
    }

# These are the production level setting that need to happen before heroku deployment
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES["default"].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
# This is a good reading subject. Do go to this url in your spare time

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# These the are static and media files handling urls, hot keys.
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# This list contains paths to where static files can be stored and should be looked for
STATICFILES_DIRS = []

# This path is where the static files will be served from in production
STATIC_ROOT = os.path.join(BASE_DIR, 'static_serve')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')