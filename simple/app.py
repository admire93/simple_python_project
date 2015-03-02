from flask import (Flask, request, abort, session, url_for, redirect, jsonify,
                   render_template)
from sqlalchemy.exc import IntegrityError

from .util import authorize, authorize_require, login_need
from .db import db
from .user import User
from .tag import Tag


__all__ = 'create_app', 'app', 'db',
config = {
    'SECRET_KEY': 'aoidfjweoif',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///simple.db',
}


app = Flask(__name__)
app.config.update(config)
db.init_app(app)


@app.route('/', methods=['GET'])
@login_need
def hello():
    return ''


@app.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def do_login():
    print(db)
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
@authorize_require
def logout():
    if session.get('token'):
        session.pop('token')
    return redirect(url_for('login'))


@app.route('/tags/', methods=['GET'])
@authorize_require
def tags():
    return ''


@app.route('/tags/', methods=['POST'])
@authorize_require
def create_tags():
    name = request.values.get('name')
    if name is None:
        abort(400)
    tag = Tag(name=name)
    db.session.add(tag)
    try:
        db.session.commit()
    except IntegrityError as exc:
        db.session.rollback()
    return jsonify(data={'tag': {'id': tag.id}}), 201


@app.route('/users/<name>/statistics/', methods=['GET'])
def user_statistics(name):
    return ''
