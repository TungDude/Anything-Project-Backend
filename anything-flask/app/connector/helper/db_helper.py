from flask import jsonify, make_response
from flask_jwt_extended import create_access_token
from ...models.users.Users import User
import bcrypt
from datetime import timedelta

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
    
    def login_user(request_body):
        if 'username' not in request_body or 'password' not in request_body:
            return jsonify({
                'error': 'Missing required fields'
            }), 400
        
        username = request_body['username']
        password = request_body['password']

        # Retrieve username from the database
        user = User.objects(username = username).first()
        if not user:
            return jsonify({
                'error': 'Username not found or invalid'
            }), 401

        # Verify password
        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({
                'error': 'Incorrect password'
            }), 401
        
        # Generate JWT token
        access_token = create_access_token(identity=username, expires_delta=timedelta(days=1))

        # Create response and store token in HTTP-only cookie
        response = make_response(jsonify({
            "message": "Login successful", 
        }), 200)
        response.set_cookie(
            "access_token_cookie", 
            access_token, 
            httponly=True, 
            secure=True,  # Set to True if using HTTPS in production
            samesite="None",  # Use Lax or None for cross-origin requests
            # domain="localhost",
            path="/"
        )
        
        return response