import json
import os

from flask import Flask
from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.db.mongodb.repository.all_messages_repository import insert_message

load_dotenv(verbose=True)


def consume_all_messages():
    consumer = KafkaConsumer(
        'messages.all',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(f'received:{message.key}:{message.value}')
        insert_message(message.value)


app = Flask(__name__)

if __name__ == '__main__':
    consume_all_messages()
    app.run()
