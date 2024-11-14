import json
import os

from flask import Flask
from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)


def consume_explosive_messages():
    consumer = KafkaConsumer(
        'messages.explosive',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(f'received:{message.key}:{message.value}')


app = Flask(__name__)

if __name__ == '__main__':
    consume_explosive_messages()
    app.run()
