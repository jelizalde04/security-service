from flask import Blueprint
from controllers.errorHandlerController import log_error, get_errors

# Create a Blueprint for error handling routes
error_handler_bp = Blueprint("errors", __name__)

# Define API routes
error_handler_bp.route("/log", methods=["POST"])(log_error)
error_handler_bp.route("/list", methods=["GET"])(get_errors)
