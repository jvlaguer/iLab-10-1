from flask import Flask
from app.routes import vqa_routes


def create_app():
    app = Flask(__name__)

    # Register Blueprints (modular routes)
    app.register_blueprint(vqa_routes)

    return app
