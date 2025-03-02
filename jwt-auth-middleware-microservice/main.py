from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from routes.authRoutes import auth_bp
from utils.swagger import setup_swagger
import logging

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure JWT authentication
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_secret")
jwt = JWTManager(app)

# Register authentication routes
app.register_blueprint(auth_bp, url_prefix="/auth")

# Set up Swagger documentation
setup_swagger(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
