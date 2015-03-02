from flask import json
from simple.tag import Tag

from .util import url_for


def test_web_denied_create_tag(fx_app):
    with fx_app.test_client() as client:
        response = client.post(url_for('create_tags'))
    assert response.status_code == 403


def test_web_create_tag(fx_app, fx_token, fx_session):
    tag_name = 'abc'
    def assert_response(response):
        assert response.status_code == 201
        assert response.data
        data = json.loads(response.data)
        assert data['data']['tag']['id']
        tag = Tag.query \
              .filter_by(id=data['data']['tag']['id']) \
              .first()
        assert tag
        assert tag_name == tag.name
        assert data['data']['tag']['id'] == tag.id

    with fx_app.test_client() as client:
        resp = client.post(url_for('create_tags', token=fx_token,
                                   name=tag_name))
        assert_response(resp)

    payload = {'token': fx_token, 'name': tag_name}
    with fx_app.test_client() as client:
        resp = client.post(url_for('create_tags'), data=payload)
        assert_response(resp)

    with fx_app.test_client() as client:
        resp = client.post(url_for('create_tags'), data=payload,
                           content_type='application/x-www-form-urlencoded')
        assert_response(resp)
