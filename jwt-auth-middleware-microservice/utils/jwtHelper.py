from flask_jwt_extended import create_access_token, create_refresh_token

def generate_tokens(user_id):
    """
    Generates access and refresh tokens for a user.
    """
    return {
        "access_token": create_access_token(identity=user_id),
        "refresh_token": create_refresh_token(identity=user_id)
    }
