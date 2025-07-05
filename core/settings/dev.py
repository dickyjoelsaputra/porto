from .base import *
from dotenv import load_dotenv

load_dotenv()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yc@op5ovy^^2ehcd48pk1(zpkw60z8b^ainnwuo*-q)g12ssk$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# --- STATIC tetap lokal ---

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "core", "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "core", "staticfiles")

# Media tetap MinIO
MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "media",
            "default_acl": "public-read",
            "file_overwrite": False
        }
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    }
}

try:
    from .local import *
except ImportError:
    pass
