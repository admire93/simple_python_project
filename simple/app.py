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

@app.route('/', methods=['GET'])
def hello():
    return ''


@app.route('/login/', methods=['GET'])
def login():
    return ''


@app.route('/login/', methods=['POST'])
def do_login():
    return ''


@app.route('/logout/', methods=['GET'])
def logout():
    return ''


@app.route('/tags/', methods=['GET'])
def tags():
    return ''


@app.route('/tags/', methods=['POST'])
def create_tags():
    return ''


@app.route('/users/<name>/statistics/', methods=['GET'])
def user_statistics(name):
    return ''
