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
