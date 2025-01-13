from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from dotenv import load_dotenv

# Initialize the MongoEngine instance
db = MongoEngine()

def create_app(config_object='instance.config.Config'):

    app = Flask(__name__)

    # Enable CORS (Cross-Origin Resource Sharing) for the frontend (React) to interact with Flask
    CORS(app, origins=["http://localhost:3000"])

    # Load environment variables from the .env file
    load_dotenv()

    # Load the configuration from the config file
    app.config.from_object(config_object)

    # # Initialize MongoEngine with the Flask app
    db.init_app(app)

    # Register Blueprints (separate routes/views into blueprints)
    from .connector.connector_controller import main
    app.register_blueprint(main)

    @app.route('/')
    def home():
        return "MongoEngine is connected!"

    return app
