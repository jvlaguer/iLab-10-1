from flask import Flask
from backend.app.config import Config
from backend.app.routes import vqa_routes

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprints (modular routes)
    app.register_blueprint(vqa_routes)

    return app