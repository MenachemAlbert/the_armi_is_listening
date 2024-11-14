import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(verbose=True)

client = MongoClient(os.environ['DB_URL'])

db = client['the_armi']
all_messages = db['all_messages']