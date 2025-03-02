from flask import Blueprint
from controllers.asyncHandlerController import create_task, get_task_status

# Create a Blueprint for async task routes
async_handler_bp = Blueprint("async", __name__)

# Define API routes
async_handler_bp.route("/task", methods=["POST"])(create_task)
async_handler_bp.route("/task/<task_id>", methods=["GET"])(get_task_status)
