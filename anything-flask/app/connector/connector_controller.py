from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from .helper.db_helper import DBHelper
from .helper.api_helper import APIHelper

main = Blueprint('main', __name__)

# Route Testing
@main.route('/api/test', methods=['GET'])
def test_api():
    return APIHelper.test_api()

# Test Protected route
@main.route('/api/protected', methods=['GET'])
@jwt_required()
def test_protected():
    current_user = get_jwt_identity()
    return jsonify({
        'message': f'Welcome, {current_user}'
    }), 200

# POST /api/users/create - Create a new user
@main.route('/api/users/create', methods=['POST'])
def create_new_user():
    body = request.get_json()
    return DBHelper.create_user(body)

# POST /api/users/login - Login a user
@main.route('/api/users/login', methods=['POST'])
def login_user():
    body = request.get_json()
    return DBHelper.login_user(body)
