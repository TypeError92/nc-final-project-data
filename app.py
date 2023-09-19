from endpoints import endpoints
from flask import Flask, request
from require_auth import require_auth

app = Flask(__name__)


# TODO: Add all endpoints here.

@app.route('/api/help')
@require_auth
def get_help():
    return endpoints


if __name__ == '__main__':
    app.run()