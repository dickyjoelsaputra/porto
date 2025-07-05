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

STORAGES = {
    "default": {
        "BACKEND": "core.storage_backends.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


try:
    from .local import *
except ImportError:
    pass
