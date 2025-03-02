from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routes.errorHandlerRoutes import error_handler_bp
from utils.swagger import setup_swagger
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "*"}})

# Register error handling routes
app.register_blueprint(error_handler_bp, url_prefix="/errors")

# Set up Swagger for API documentation
setup_swagger(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
