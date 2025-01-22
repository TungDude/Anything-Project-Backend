# from . import db
from mongoengine import Document, StringField

class User(Document):
    # Fields that represent the user data
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

    # Optional: define a string representation of the model
    def __str__(self):
        return f"User({self.username}, {self.email}, {self.age})"
    
    def to_json(self):
        # Helper method to convert the object into a JSON-serializable dictionary
        return {
            'id': str(self.id),  # Convert ObjectId to string
            'username': self.username,
        }
