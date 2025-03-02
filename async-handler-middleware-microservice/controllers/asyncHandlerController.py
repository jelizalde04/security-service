from flask import request, jsonify
from services.asyncHandlerService import AsyncHandlerService

# Initialize async service
async_service = AsyncHandlerService()

def create_task():
    """
    Creates a new asynchronous task.
    """
    data = request.json
    task_type = data.get("task_type")

    if not task_type:
        return jsonify({"error": "Missing task_type field"}), 400

    task_id = async_service.process_task(task_type)
    return jsonify({"message": "Task started", "task_id": task_id}), 202

def get_task_status(task_id):
    """
    Retrieves the status of an asynchronous task.
    """
    status = async_service.get_task_status(task_id)
    return jsonify({"task_id": task_id, "status": status}), 200
