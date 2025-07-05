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

try:
    from .local import *
except ImportError:
    pass
