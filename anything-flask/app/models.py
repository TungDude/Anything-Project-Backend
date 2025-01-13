# from . import db
from mongoengine import Document, StringField, IntField

class User(Document):
    # Fields that represent the user data
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    age = IntField(required=False)

    # Optional: define a string representation of the model
    def __str__(self):
        return f"User({self.username}, {self.email}, {self.age})"
    
    def to_json(self):
        # Helper method to convert the object into a JSON-serializable dictionary
        return {
            'id': str(self.id),  # Convert ObjectId to string
            'username': self.username,
            'email': self.email,
            'age': self.age
        }
