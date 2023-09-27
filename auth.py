import os
from flask import make_response, request
from functools import wraps

username, password = os.getenv('API_USERNAME'), os.getenv('API_PASSWORD')


def auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if (auth and
                ((auth.username, auth.password == username, password):
            return f(*args, **kwargs)
        return make_response('You are not logged in!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated
