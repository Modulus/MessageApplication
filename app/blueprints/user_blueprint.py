from flask import Blueprint, request

__author__ = 'johska'

api = Blueprint('user_api', __name__)

@api.route('/<string:id>', methods=['GET'])
def get_user(id):
    return None

@api.route('/', methods=['POST'])
def create_user():
    username = request.args['username']
    password = request.args['password']

    x = 0