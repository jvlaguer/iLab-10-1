import logging
from flask import Flask, request
from backend.app.routes.vqa_routes import vqa_routes
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, origins="http://localhost:5173", supports_credentials=True)

    # Set up logging configuration
    logging.basicConfig(
        filename="app.log",  # Log to 'app.log' file; you can remove 'filename' to log to the console
        level=logging.DEBUG,  # Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger(__name__)

    # Log every request before handling it
    @app.before_request
    def log_request_info():
        logger.info(f"Incoming request: {request.method} {request.url}")

    # Log the response after it's handled
    @app.after_request
    def log_response_info(response):
        logger.info(f"Outgoing response: {response.status}")
        return response

    # Register the blueprint
    app.register_blueprint(vqa_routes)

    @app.route("/")
    def home():
        logger.info("Home route accessed")  # Example log for the home route
        return "Welcome to the VQA system!"

    return app


app = create_app()
