# API Error Handler Microservice

## Description
This microservice provides centralized error logging and handling for APIs. It allows recording errors with detailed metadata, including timestamps, endpoints, and error types.

## Endpoints
### **POST /errors/log-error**
Logs an error into the database.
#### Request Body:
```json
{
  "error_message": "Something went wrong",
  "error_type": "ValidationError",
  "endpoint": "/api/v1/resource",
  "status_code": 400
}
