import uuid

class AsyncTask:
    """
    Represents an asynchronous task.
    """
    def __init__(self, task_type):
        self.task_id = str(uuid.uuid4())  # Generate a unique task ID
        self.task_type = task_type
