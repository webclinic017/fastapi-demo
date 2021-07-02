import os
from celery import Celery


def create_celery():
    CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST') or '127.0.0.1'
    CACHE_REDIS_PORT = os.environ.get('CACHE_REDIS_PORT') or 63790
    CACHE_REDIS_DB = os.environ.get('CACHE_REDIS_DB') or '0'
    CACHE_REDIS_PASSWORD = os.environ.get('CACHE_REDIS_PASSWORD') or 'greenvalley'

    # 'redis://auth:password@redishost:6379/0'
    CELERY_BROKER_URL = 'redis://auth:%s@%s:%s/12' % (CACHE_REDIS_PASSWORD, CACHE_REDIS_HOST, CACHE_REDIS_PORT,)
    CELERY_RESULT_BACKEND = 'redis://auth:%s@%s:%s/13' % (CACHE_REDIS_PASSWORD, CACHE_REDIS_HOST, CACHE_REDIS_PORT,)
    celery = Celery("celery", backend=CELERY_BROKER_URL, broker=CELERY_RESULT_BACKEND)
    return celery

celery = create_celery()
