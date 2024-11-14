from flask import Flask

from app.db.mongodb.routes.all_messages_route import email_blueprint
from app.db.psql.database import init_db

app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    app.register_blueprint(email_blueprint, url_prefix="/api/email")
    app.run()
