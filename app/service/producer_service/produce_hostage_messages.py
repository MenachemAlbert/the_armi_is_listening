import json
import os

from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)


def produce_hostage_messages(message):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(
        'messages.hostage',
        value=message,
        key=message['email'].encode('utf-8')
    )
