from flask import Blueprint, jsonify

from app.service.most_common_servise import get_most_common

most_common_blueprint = Blueprint('most_common', __name__)


@most_common_blueprint.route('/', methods=['GET'])
def most_common_in_sentence():
    most_word = get_most_common()
    return jsonify(f"the most word is {most_word[0]} which appears {most_word[1]} times")
