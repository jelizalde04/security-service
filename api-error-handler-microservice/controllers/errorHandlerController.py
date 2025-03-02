from flask import request, jsonify
from services.errorHandlerService import ErrorHandlerService

# Initialize error handling service
error_service = ErrorHandlerService()

def log_error():
    """
    Logs an error received from any microservice.
    """
    data = request.json
    service_name = data.get("service")
    error_message = data.get("error")

    if not service_name or not error_message:
        return jsonify({"error": "Missing required fields"}), 400

    error_service.save_error(service_name, error_message)
    return jsonify({"message": "Error logged successfully"}), 201

def get_errors():
    """
    Retrieves all logged errors.
    """
    errors = error_service.get_all_errors()
    return jsonify(errors), 200
