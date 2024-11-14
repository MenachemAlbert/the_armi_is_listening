from flask import Flask

from app.routes.all_messages_route import email_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(email_blueprint, url_prefix="/api/email")
    app.run()
