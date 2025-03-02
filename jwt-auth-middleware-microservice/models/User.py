import uuid

class User:
    """
    Represents a user in the system.
    """
    def __init__(self, email, password):
        self.id = str(uuid.uuid4())  # Generate a unique user ID
        self.email = email
        self.password = password  # Store hashed password
