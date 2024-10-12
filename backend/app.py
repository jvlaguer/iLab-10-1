import os
from flask import Flask
from backend.app.routes.vqa_routes import vqa_routes

def create_app():
    app = Flask(__name__)
    
    # Register the blueprint
    app.register_blueprint(vqa_routes)
    
    @app.route('/')
    def home():
        return "Welcome to the VQA system!"
    
    return app

if __name__ == "__main__":
    app = create_app()
    
    # Dynamically bind to the port provided by Render (or default to 5000 for local dev)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)