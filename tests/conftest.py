from pytest import fixture, yield_fixture

from simple.app import app, db
from simple.user import User
from simple.util import authorize

@fixture
def fx_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['TESTING'] = True
    return app


@yield_fixture
def fx_session(fx_app):
    with fx_app.app_context():
        db.create_all()
        yield db.session
        db.drop_all()


@fixture
def fx_user(fx_session):
    name = 'kanghyoj'
    user = User(name=name)
    fx_session.add(user)
    fx_session.commit()
    return user


@fixture
def fx_token(fx_user):
    return authorize(fx_user)
