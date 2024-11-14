from flask import Blueprint, request, jsonify

from app.service.user_service import get_user_data_by_email

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user_data', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        user_data = get_user_data_by_email(email)
        if not user_data:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user_data)

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
