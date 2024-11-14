import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.psql.models import Base

load_dotenv(verbose=True)

SQL_URI = os.environ['DATABASE_URL']

engine = create_engine(SQL_URI)
session_maker = sessionmaker(bind=engine)


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

