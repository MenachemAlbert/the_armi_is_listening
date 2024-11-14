from sqlalchemy.exc import SQLAlchemyError
from app.db.psql.database import session_maker
from app.db.psql.models import User, Location, DeviceInfo


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
