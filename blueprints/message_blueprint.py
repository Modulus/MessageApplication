from flask import Blueprint

__author__ = 'johska'

api = Blueprint('message_api', __name__)

@api.route('/<string:id>', methods=['GET'])
def get_message(id):
    return None