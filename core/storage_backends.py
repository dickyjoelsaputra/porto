from storages.backends.s3boto3 import S3Boto3Storage
import logging

logger = logging.getLogger(__name__)


class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
    signature_version = 's3v4'

    def _save(self, name, content):
        logger.info(f"Uploading media file: {name}")
        return super()._save(name, content)


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"
    file_overwrite = True
    signature_version = 's3v4'

    def _save(self, name, content):
        logger.info(f"Uploading static file: {name}")
        return super()._save(name, content)
