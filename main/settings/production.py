from main.settings.shared import *
import os
import django_heroku
import dj_database_url

# Heroku config variables
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']
DJANGO_ALLOWED_HOSTS = ['.herokuapp.com']

# Use PostgreSQL in place of SQLite3 for production
DATABASES = {
    'default': dj_database_url.config()
    }

USE_S3 = os.environ['USE_S3']
if USE_S3:
    AWS_LOCATION = 'static'
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    # Tell django-storages the domain to use to refer to static files
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    DEFAULT_FILE_STORAGE = 'main.storage_backends.MediaStorage'
    AWS_DEFAULT_ACL = None
    # AWS Static file handling
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'  # for AWS S3 use
    STATICFILES_STORAGE = 'main.storage_backends.StaticStorage'         # for AWS S3 use
    STATICFILES_FINDERS = (                                             # for AWS S3 use
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
else:
    # Local static file handling
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')







EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
EMAIL_PORT = os.environ['EMAIL_PORT']

# Activate Django-Heroku
django_heroku.settings(locals())

# Workaround the PostgreSQL mandate for SSL
options = DATABASES['default'].get('OPTIONS', ())
options.pop('sslmode', None)