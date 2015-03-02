from functools import wraps
from datetime import datetime

from itsdangerous import JSONWebSignatureSerializer, BadSignature
from flask import current_app, abort, request, g, redirect, url_for

from .user import User


__all__ = 'authorize_require', 'authorize', 'authorize_request', 'login_need',


def authorize_require(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        g.current_user = authorize_request()
        if g.current_user is None:
            abort(403)
        elif not g.current_user:
            abort(404)
        return f(*args, **kwargs)
    return decorator


def login_need(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        g.current_user = authorize_request()
        if not g.current_user:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorator



def authorize_request():
    token = request.values.get('token')
    auth_header = request.headers.get('Authorization')
    header_prefix = 'Token '
    if auth_header and auth_header.startswith(header_prefix):
        token = auth_header[len(header_prefix):]
    if token is None:
        return None
    elif not authorize(token):
        return None
    data = authorize(token)
    user = User.query \
           .filter_by(name=data['user.name']) \
           .first()
    return user


def authorize(user):
    s = JSONWebSignatureSerializer(current_app.config.get('SECRET_KEY'))
    if isinstance(user, User):
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        payload = {'user.name': user.name, 'login_at': now}
        return s.dumps(payload).decode('utf-8')
    elif isinstance(user, str):
        try:
            return s.loads(user)
        except BadSignature as exc:
            pass
    return None
