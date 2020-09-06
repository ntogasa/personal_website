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
    'default': dj_database_url.config(os.environ('DATABASE_URL'))
    }


USE_S3 = os.environ['USE_S3']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

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