import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

FILTER_STATE_CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 86400,
    "CACHE_KEY_PREFIX": "superset_filter_cache",
    "CACHE_REDIS_URL": "redis://localhost:6379/0",
}

ENABLE_PROXY_FIX = True

SECRET_KEY = os.environ.get("SECRET_KEY")
SQL_ALCHEMY_DATABASE_URI = os.environ.get("SQL_ALCHEMY_DATABASE_URI")
