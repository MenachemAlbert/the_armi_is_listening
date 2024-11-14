from flask import Blueprint, request, jsonify

from app.repository.all_messages_repository import insert_message

email_blueprint = Blueprint('email', __name__)


@email_blueprint.route('/', methods=['POST'])
def add_messages():
    message = request.json
    print(message)
    insert_message(message)
    return jsonify("messages inserted"), 201
