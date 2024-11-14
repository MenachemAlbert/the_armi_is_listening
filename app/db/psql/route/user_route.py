from dictalchemy.utils import asdict
from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload

from app.db.psql.database import session_maker
from app.db.psql.models import User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user_data', methods=['GET'])
def get_user_data_by_email():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400

    try:
        with session_maker() as session:
            user = session.query(User).options(
                joinedload(User.location),
                joinedload(User.device_info),
                joinedload(User.explosive_sentences)
            ).filter(User.email == email).first()

            if not user:
                return jsonify({"error": "User not found"}), 404

            return jsonify({
                "username": user.username,
                "email": user.email,
                "location": asdict(user.location),
                "device_info": asdict(user.device_info),
                "explosive_sentences": [sentence.sentence for sentence in user.explosive_sentences],
                "hostage_sentences": [sentence.sentence for sentence in user.hostage_sentences]
            })

    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
