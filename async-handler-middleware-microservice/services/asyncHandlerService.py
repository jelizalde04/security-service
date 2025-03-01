from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL
)

@celery_app.task
def async_task(data):
    return f"Processed {data} asynchronously"