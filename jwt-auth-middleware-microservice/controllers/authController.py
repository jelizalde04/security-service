from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from services.authService import AuthService

# Initialize authentication service
auth_service = AuthService()

def login():
    """
    Authenticate user and generate JWT tokens.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = auth_service.authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT access and refresh tokens
    access_token = create_access_token(identity=user["id"])
    refresh_token = create_refresh_token(identity=user["id"])
    
    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

def register():
    """
    Register a new user with hashed password.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = auth_service.create_user(email, password)
    return jsonify(user), 201

@jwt_required(refresh=True)
def refresh_token():
    """
    Refresh JWT access token.
    """
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_token}), 200
