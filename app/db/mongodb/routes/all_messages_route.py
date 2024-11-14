from flask import Blueprint, request, jsonify

from app.service.producer_service.producer_all_messages import produce_all_messages

email_blueprint = Blueprint('email', __name__)


@email_blueprint.route('/', methods=['POST'])
def add_messages():
    message = request.json
    produce_all_messages(message)
    return jsonify("messages inserted"), 201
