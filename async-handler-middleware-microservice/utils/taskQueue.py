from celery import Celery
import time

# Initialize Celery
celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def execute_async_task(task_id, task_type):
    """
    Simulates an async task execution.
    """
    time.sleep(5)  # Simulate long-running task
    return f"Task {task_id} of type {task_type} completed."
