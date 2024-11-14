import json
import os

from flask import Flask
from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.db.psql.repository.psql_repository import insert_user

load_dotenv(verbose=True)


def consume_explosive_messages():
    consumer = KafkaConsumer(
        'messages.explosive',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )
    for message in consumer:
        insert_user(message.value)
        print(f'received:{message.key}:{message.value}')


app = Flask(__name__)

if __name__ == '__main__':
    consume_explosive_messages()
    app.run()
