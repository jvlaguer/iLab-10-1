from flask import Flask
from backend.app.routes.vqa_routes import vqa_routes


def create_app():
    app = Flask(__name__)

    # Register Blueprints (modular routes)
    app.register_blueprint(vqa_routes)

    return app

# The application object
app = create_app()
