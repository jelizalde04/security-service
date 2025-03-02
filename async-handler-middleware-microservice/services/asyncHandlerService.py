from models.AsyncTask import AsyncTask
from utils.taskQueue import execute_async_task
from utils.logger import log_to_file

class AsyncHandlerService:
    """
    Manages asynchronous task execution and monitoring.
    """
    def __init__(self):
        self.task_store = {}  # In-memory database for task tracking

    def process_task(self, task_type):
        """
        Initiates an asynchronous task and stores its ID.
        """
        task = AsyncTask(task_type)
        self.task_store[task.task_id] = "PENDING"

        # Execute task asynchronously
        execute_async_task.delay(task.task_id, task_type)

        # Log task creation
        log_to_file(f"Task Created: {task.task_id} - {task_type}")

        return task.task_id

    def get_task_status(self, task_id):
        """
        Returns the status of a given task.
        """
        return self.task_store.get(task_id, "UNKNOWN")
