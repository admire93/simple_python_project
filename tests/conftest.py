from pytest import fixture, yield_fixture

from simple.app import app, db


@fixture
def fx_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    return app


@yield_fixture
def fx_session(fx_app):
    with fx_app.app_context():
        db.create_all()
        yield db.session
        db.drop_all()
