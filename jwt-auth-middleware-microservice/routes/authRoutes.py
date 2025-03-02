from flask import Blueprint
from controllers.authController import login, register, refresh_token

# Create a Blueprint for authentication routes
auth_bp = Blueprint("auth", __name__)

# Define authentication endpoints
auth_bp.route("/login", methods=["POST"])(login)
auth_bp.route("/register", methods=["POST"])(register)
auth_bp.route("/refresh", methods=["POST"])(refresh_token)
