import django_heroku

from .base import *

AWS_ACCESS_KEY_ID = 'AKIA2IWSN5VSZBZPGL7W'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sibtc-static-500'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())
