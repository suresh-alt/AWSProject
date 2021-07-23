from storages.backends.s3boto3 import S3Boto3Storage

class DynamicFiles(S3Boto3Storage):
    locaton = 'media'
    file_overwrite = False
