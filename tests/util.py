from flask import url_for as f_url_for

from simple.app import app

def url_for(*args, **kwargs):
    with app.app_context():
        return f_url_for(*args, **kwargs)
