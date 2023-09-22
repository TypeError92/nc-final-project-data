import auth
from controllers.question_controllers import get_questions
from endpoints import endpoints
from flask import Flask, make_response, request

app = Flask(__name__)


# TODO: Add all endpoints here.

@app.route('/api')
@auth.admin
def api():
    return endpoints


@app.route('/api/questions')
def api_questions():
    return get_questions()


@app.route('/api/users', methods=['POST'])
def api_users():
    pass


@app.route('/api/users/<username>', methods=['GET', 'PATCH', 'DELETE'])
@auth.user
def api_users__username(username):
    if request.method == 'GET':
        return make_response(
            {"user": {"username": username}},
            200
        )
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass


@app.route('/api/leaderboard', methods=['GET'])
@auth.user
def get_leaderboard():
    return make_response(
        {"entries": [
            {"rank": 1, "username": "phil", "score": 1234},
            {"rank": 2, "username": "charlotte", "score": 1111},
            {"rank": 3, "username": "chris", "score": 999}
        ]},
        200
    )


@app.route('/api/leaderboard', methods=['PATCH'])
@auth.admin
# TODO: accept user/score pairs in request body
def patch_leaderboard():
    return make_response(
        {},
        200
    )


if __name__ == '__main__':
    app.run()
