from flask import jsonify
from ...models.users.Users import User
import bcrypt

class DBHelper():
    def create_user(request_body):
        # Validate request_body
        if 'username' not in request_body or 'password' not in request_body:
            return jsonify({
                'error': 'Missing required fields'
            }), 400

        user = User(
            username=request_body['username'],
            password=bcrypt.hashpw(request_body['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        user.save()  # Save the user to MongoDB

        return jsonify({
            'message': 'User created successfully', 
        }), 201