from flask import jsonify
from ...models import User

class DBHelper():
    def create_user(request_body):
        # Validate request_body
        if 'username' not in request_body or 'email' not in request_body:
            return jsonify({
                'error': 'Missing required fields'
            }), 400

        user = User(
            username=request_body['username'],
            email=request_body['email'],
            age=request_body.get('age', None)
        )
        user.save()  # Save the user to MongoDB

        return jsonify({
            'message': 'User created successfully', 
        }), 201