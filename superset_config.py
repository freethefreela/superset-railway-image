import logging
import os

logger = logging.getLogger()

PYTHONPATH = os.environ.get("PYTHONPATH")

RATELIMIT_STORAGE_URI = os.environ.get("SUPERSET_CACHE_REDIS_URL")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SUPERSET_CACHE_REDIS_URL = os.environ.get("SUPERSET_CACHE_REDIS_URL")
SUPERSET_LOAD_EXAMPLES = os.environ.get("SUPERSET_LOAD_EXAMPLES")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_URL = os.environ.get("REDIS_URL")

SUPERSET_ENV = os.environ.get("SUPERSET_ENV")
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY")
SUPERSET_PORT = os.environ.get("SUPERSET_PORT")
SUPERSET_CACHE_REDIS_URL = os.environ.get("SUPERSET_CACHE_REDIS_URL")
ENABLE_PROXY_FIX = True

if not REDIS_HOST:
    logger.error("REDIS_HOST is not set")
    exit(1)

if not REDIS_PORT:
    logger.error("REDIS_PORT is not set")
    exit(1)

if not REDIS_URL:
    logger.error("REDIS_URL is not set")
    exit(1)

if not SUPERSET_ENV:
    logger.error("SUPERSET_ENV is not set")
    exit(1)

if not SECRET_KEY:
    logger.error("SUPERSET_SECRET_KEY is not set")
    exit(1)

if not SUPERSET_PORT:
    logger.error("SUPERSET_PORT is not set")
    exit(1)

if not SUPERSET_CACHE_REDIS_URL:
    logger.error("SUPERSET_CACHE_REDIS_URL is not set")
    exit(1)

if not SQLALCHEMY_DATABASE_URI:
    logger.error("SQLALCHEMY_DATABASE_URI is not set")
    exit(1)

if not RATELIMIT_STORAGE_URI:
    logger.error("RATELIMIT_STORAGE_URI is not set")
    exit(1)

if not PYTHONPATH:
    logger.error("PYTHONPATH is not set")
    exit(1)


FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_URL": REDIS_URL,
}

DATA_CACHE_CONFIG = CACHE_CONFIG


class CeleryConfig(object):
    BROKER_URL = SUPERSET_CACHE_REDIS_URL + "/1"
    CELERY_IMPORTS = ("superset.sql_lab",)
    CELERY_RESULT_BACKEND = SUPERSET_CACHE_REDIS_URL + "/0"
    CELERY_ANNOTATIONS = {"tasks.add": {"rate_limit": "10/s"}}


CELERY_CONFIG = CeleryConfig
