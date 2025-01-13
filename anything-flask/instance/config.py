import os
from dotenv import load_dotenv
import certifi

# Load environment variables from .env file
load_dotenv()

class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY')  # Use default if not set
    MONGO_URI = os.getenv('MONGO_URI')  # Default URI if not set in .env

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = os.getenv('MONGO_URI')
    MONGODB_SETTINGS = {
        'db': 'my_db', 
        'host': os.getenv('MONGO_URI'), 
        'tlsCAFile': certifi.where(), 
    }

class ProductionConfig(Config):
    MONGO_URI = 'mongodb://user:password@prod_host:27017/prod_db'