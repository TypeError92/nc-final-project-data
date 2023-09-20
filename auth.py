from flask import make_response, request
from functools import wraps


def user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'user' and auth.password == 'user':
            return f(*args, **kwargs)
        return make_response('You are not logged in!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated


def admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'admin' and auth.password == 'admin':
            return f(*args, **kwargs)
        return make_response('You are not logged in!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated
