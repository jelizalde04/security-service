from bcrypt import hashpw, gensalt, checkpw

def hash_password(password):
    """
    Hashes a password using bcrypt.
    """
    return hashpw(password.encode(), gensalt()).decode()

def verify_password(password, hashed_password):
    """
    Verifies a password against its hashed version.
    """
    return checkpw(password.encode(), hashed_password.encode())
