from app.db.psql.database import session_maker
from app.db.psql.models import ExplosiveSentence, HostageSentence


def get_all_explosive_sentences():
    with session_maker() as session:
        return session.query(ExplosiveSentence).all()


def get_all_hostage_sentences():
    with session_maker() as session:
        return session.query(HostageSentence).all()
