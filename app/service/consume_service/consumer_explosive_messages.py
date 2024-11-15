import json
import os

from flask import Flask
from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.db.psql.repository.psql_repository import insert_user, add_explosive_sentences

load_dotenv(verbose=True)


def consume_explosive_messages():
    consumer = KafkaConsumer(
        'messages.explosive',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )
    for message in consumer:
        try:
            inserted_user = insert_user(message.value)
            if inserted_user is not None:
                add_explosive_sentences(inserted_user, message.value['sentences'])

        except Exception as e:
            print(f"Unexpected error while processing message: {e}")


app = Flask(__name__)

if __name__ == '__main__':
    consume_explosive_messages()
    app.run()
