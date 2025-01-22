from flask import Blueprint, request
from .helper.db_helper import DBHelper
from .helper.api_helper import APIHelper

main = Blueprint('main', __name__)

# Route Testing
@main.route('/api/test', methods=['GET'])
def test_api():
    return APIHelper.test_api()

# POST /api/users/create - Create a new user
@main.route('/api/users/create', methods=['POST'])
def create_new_user():
    body = request.get_json()
    return DBHelper.create_user(body)
