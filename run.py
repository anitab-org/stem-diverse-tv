from flask import Flask
import app


def create_app() -> Flask:
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///local_data.db"
    app.url_map.strict_slashes = False
    
    from app.apis import api
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
