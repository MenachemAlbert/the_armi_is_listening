from app.db.mongodb.database import all_messages


def insert_message(message):
    all_messages.insert_one(message)
