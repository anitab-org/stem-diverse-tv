import firebase_admin
from dotenv import load_dotenv, find_dotenv
from firebase_admin import credentials
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///local_data.db"
    app.url_map.strict_slashes = False

    load_dotenv(find_dotenv())

    """ Download service file from firebase and put it in project root directory """
    cred = credentials.Certificate("google-credentials.json")
    firebase_admin.initialize_app(cred)

    from app.api.controllers import api

    api.init_app(app)

    from app.database.sqlalchemy_extension import db

    db.init_app(app)

    return app


application = create_app()


@application.before_first_request
def create_tables():
    from app.database.sqlalchemy_extension import db

    db.create_all()


if __name__ == "__main__":
    application.run(port=5000)
