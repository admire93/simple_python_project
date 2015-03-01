from flask import Flask, request, abort, session, url_for, redirect
from sqlalchemy.exc import IntegrityError

from .util import authorize
from .db import db
from .user import User


__all__ = 'create_app', 'app', 'db',
config = {
    'SECRET_KEY': 'aoidfjweoif',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////simple.db',
    'SERVER_NAME': 'localhost',
}


def create_app():
    app = Flask(__name__)
    app.config.update(config)
    db.init_app(app)
    return app


app = create_app()


@app.route('/', methods=['GET'])
def hello():
    return ''


@app.route('/login/', methods=['GET'])
def login():
    return ''


@app.route('/login/', methods=['POST'])
def do_login():
    name = request.values.get('username')
    if not name:
        abort(400)
    user = User.query \
           .filter_by(name=name) \
           .first()
    if not user:
        user = User(name=name)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError as exc:
            print(exc)
            db.session.rollback()
            abort(500)
    session['token'] = authorize(user)
    return redirect(url_for('hello'))


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
