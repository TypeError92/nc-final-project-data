from flask import make_response, request
from functools import wraps


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)
        return make_response('You are not logged in!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated
