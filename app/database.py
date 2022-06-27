from redis_om import get_redis_connection
from .config import settings

redis = get_redis_connection(
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    password=settings.DB_PASSWORD,
    decode_responses=True
)
