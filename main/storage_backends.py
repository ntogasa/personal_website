from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    """Custom storage class that ensures media files are stored seperately from static files"""
    location = settings.MEDIAFILES_LOCATION


class StaticStorage(S3Boto3Storage):
    """Custom storage class that ensures static files are stored separately from media files."""
    location = settings.STATICFILES_LOCATION