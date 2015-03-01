from datetime import datetime

from itsdangerous import JSONWebSignatureSerializer, BadSignature
from flask import current_app

from .user import User


def login_required():
    return ''


def authorize(user):
    s = JSONWebSignatureSerializer(current_app.config.get('SECRET_KEY'))
    if isinstance(user, User):
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        return s.dumps({'user.name': user.name, 'login_at': now})
    else:
        try:
            return s.loads(user)
        except BadSignature as exc:
            return None
