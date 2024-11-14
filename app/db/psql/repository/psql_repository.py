from sqlalchemy.exc import SQLAlchemyError
from app.db.psql.database import session_maker
from app.db.psql.models import User, Location, DeviceInfo, ExplosiveSentence, HostageSentence


def create_user(user_data):
    return User(
        username=user_data['username'],
        email=user_data['email']
    )


def create_location(location_data, user):
    return Location(
        latitude=location_data['latitude'],
        longitude=location_data['longitude'],
        city=location_data['city'],
        country=location_data['country'],
        user=user
    )


def create_device_info(device_data, user):
    return DeviceInfo(
        browser=device_data['browser'],
        os=device_data['os'],
        device_id=device_data['device_id'],
        user=user
    )


def insert_user(user_data):
    try:
        with session_maker() as session:
            user = create_user(user_data)
            location = create_location(user_data['location'], user)
            device_info = create_device_info(user_data['device_info'], user)

            user.location = location
            user.device_info = device_info

            session.add(user)
            session.add(location)
            session.add(device_info)

            session.commit()
            session.refresh(user)
            return user.id

    except SQLAlchemyError as e:
        print(f"SQLAlchemyError: {e}")
        return None


def add_explosive_sentences(user_id, sentences):
    try:
        with session_maker() as session:
            user = session.query(User).filter_by(id=user_id).first()
            if user is None:
                print(f"User with id {user_id} not found.")
                return None

            for sentence in sentences:
                sentence = ExplosiveSentence(sentence=sentence, user=user)
                session.add(sentence)

            session.commit()
            print(f"Added explosive sentences for user {user_id}.")
            return True

    except SQLAlchemyError as e:
        print(f"SQLAlchemyError: {e}")
        return None


def add_hostage_sentences(user_id, sentences):
    try:
        with session_maker() as session:
            user = session.query(User).filter_by(id=user_id).first()
            if user is None:
                print(f"User with id {user_id} not found.")
                return None

            for sentence in sentences:
                sentence = HostageSentence(sentence=sentence, user=user)
                session.add(sentence)

            session.commit()
            print(f"Added hostage sentences for user {user_id}.")
            return True

    except SQLAlchemyError as e:
        print(f"SQLAlchemyError: {e}")
        return None
