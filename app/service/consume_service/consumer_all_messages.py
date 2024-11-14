import json
import os

from flask import Flask
from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.db.mongodb.repository.all_messages_repository import insert_message
from app.service.producer_service.produce_explosive_messages import produce_explosive_messages
from app.service.producer_service.produce_hostage_messages import produce_hostage_messages
from app.service.suspicious_content_service import contains_suspicious_content

load_dotenv(verbose=True)


def consume_all_messages():
    consumer = KafkaConsumer(
        'messages.all',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )
    for message in consumer:
        insert_message(message.value)

        if 'sentences' in message.value:
            sentences = message.value['sentences']
            message.value['_id'] = str(message.value['_id'])

            if contains_suspicious_content(sentences, 'hostage'):
                produce_hostage_messages(message.value)

            if contains_suspicious_content(sentences, 'explos'):
                produce_explosive_messages(message.value)


app = Flask(__name__)

if __name__ == '__main__':
    consume_all_messages()
    app.run()
