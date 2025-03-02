from flask_swagger_ui import get_swaggerui_blueprint

def setup_swagger(app):
    """
    Sets up Swagger UI for API documentation.
    """
    SWAGGER_URL = "/docs"
    API_URL = "/static/swagger.json"
    swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "JWT Auth API"})
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)
