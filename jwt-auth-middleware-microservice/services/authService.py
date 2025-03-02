from models.User import User
from utils.cryptoHelper import hash_password, verify_password

class AuthService:
    """
    Handles user authentication and registration.
    """
    def __init__(self):
        self.users = []  # Simulated in-memory database

    def create_user(self, email, password):
        """
        Creates a new user with a hashed password.
        """
        if any(user.email == email for user in self.users):
            return {"error": "User already exists"}
        
        hashed_password = hash_password(password)
        new_user = User(email, hashed_password)
        self.users.append(new_user)
        
        return {"message": "User successfully registered"}

    def authenticate_user(self, email, password):
        """
        Authenticates a user by verifying password hash.
        """
        user = next((u for u in self.users if u.email == email), None)
        if user and verify_password(password, user.password):
            return {"id": user.id, "email": user.email}
        return None
