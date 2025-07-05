from .base import *

DEBUG = False

# Static & Media pakai MinIO
STORAGES = {
    "default": {
        "BACKEND": "core.storage_backends.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "core.storage_backends.StaticStorage",
    },
}

STATIC_URL = f"{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/media/"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yc@op5ovy^^2ehcd48pk1(zpkw60z8b^ainnwuo*-q)g12ssk$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["103.197.188.89","dickyjoel.icu","https://dickyjoel.icu"]

try:
    from .local import *
except ImportError:
    pass
