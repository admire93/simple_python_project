from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


__all__ = 'create_app', 'app', 'db',
config = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////simple.db'
}


def create_app():
    app = Flask(__name__)
    app.config.update(config)
    return app


app = create_app()
db = SQLAlchemy(app)
