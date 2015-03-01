from flask import json, current_app, session

from simple.user import User
from simple.app import db
from simple.util import authorize

from .util import url_for


def test_do_login(fx_app, fx_session, fx_user):
    print(fx_user.name)
    with fx_app.test_client() as client:
        response = client.post(
            url_for('do_login'),
            data={'username': fx_user.name},
            content_type='application/x-www-form-urlencoded')
        assert response.status_code == 302
        assert session.get('token')
        assert session.get('token') == authorize(fx_user)


def test_do_login_without_already_created(fx_app, fx_session):
    name = 'anom'
    with fx_app.test_client() as client:
        response = client.post(
            url_for('do_login'),
            data={'username': name},
            content_type='application/x-www-form-urlencoded')
        assert response.status_code == 302
        assert session.get('token')
        sess_token = session.get('token')
    user = User.query \
           .filter_by(name=name) \
           .first()
    assert user
    assert user.name == name
    token = authorize(user)
    assert sess_token == token


def test_400_do_login(fx_app, fx_session):
    with fx_app.test_client() as client:
        response = client.post(
            url_for('do_login'),
            content_type='application/x-www-form-urlencoded')
        assert response.status_code == 400
