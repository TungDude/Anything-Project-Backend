from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Initialize the MongoEngine instance
db = MongoEngine()

def create_app(config_object='instance.config.Config'):

    app = Flask(__name__)

    jwt = JWTManager(app)

    # Enable CORS (Cross-Origin Resource Sharing) for the frontend (React) to interact with Flask
    CORS(app, supports_credentials=True, origins=["http://localhost:3000"])
    # CORS(app)

    # Load environment variables from the .env file
    load_dotenv()

    # Load the configuration from the config file
    app.config.from_object(config_object)
    # Secret key for JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]  # Store JWT in cookies
    app.config["JWT_COOKIE_SECURE"] = False  # Set to True if using HTTPS
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Disable CSRF for testing

    # # Initialize MongoEngine with the Flask app
    db.init_app(app)

    # Register Blueprints (separate routes/views into blueprints)
    from .connector.connector_controller import main
    app.register_blueprint(main)

    @app.route('/')
    def home():
        return "Flask server is running! MongoEngine is connected!"

    return app
