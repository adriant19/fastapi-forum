from redis_om import HashModel
from datetime import datetime
from app.database import redis


# -- Order Model ---------------------------------------------------------------

class Post(HashModel):

    title: str
    content: str
    replies: int = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Meta:
        database = redis


class Reply(HashModel):

    post_id: str
    content: str
    created_at: datetime = datetime.now()

    class Meta:
        database = redis
