from .base import *

DEBUG = False

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "core", "static"),
]

# Static dan media semua ke MinIO
STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/"
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "media",
            "default_acl": "public-read",
            "file_overwrite": False,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {"location": "static", "default_acl": "public-read"},
    },
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yc@op5ovy^^2ehcd48pk1(zpkw60z8b^ainnwuo*-q)g12ssk$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [
    "103.197.188.89",
    "dickyjoel.icu",
    "https://dickyjoel.icu",
]

try:
    from .local import *
except ImportError:
    pass
