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
    app.run(debug=True)