# app/services/user_service.py
from sqlalchemy.orm import joinedload
from app.db.psql.models import User
from dictalchemy.utils import asdict
from app.db.psql.database import session_maker


def get_user_data_by_email(email):
    try:
        with session_maker() as session:
            user = session.query(User).options(
                joinedload(User.location),
                joinedload(User.device_info),
                joinedload(User.explosive_sentences),
                joinedload(User.hostage_sentences)
            ).filter(User.email == email).first()

            if not user:
                return None

            return {
                "username": user.username,
                "email": user.email,
                "location": asdict(user.location),
                "device_info": asdict(user.device_info),
                "explosive_sentences": [sentence.sentence for sentence in user.explosive_sentences],
                "hostage_sentences": [sentence.sentence for sentence in user.hostage_sentences]
            }
    except Exception as e:
        raise Exception(f"Error fetching user data: {str(e)}")
