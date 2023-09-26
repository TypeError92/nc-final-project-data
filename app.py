import auth
from controllers.dev_controllers import get_num_of_connections
from controllers import get_questions, get_user, post_user
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


@app.route('/api/stats/num-of-connections')
@auth.admin
def stats_num_of_connections():
    return get_num_of_connections()


@app.route('/api/users/sign-in', methods=['POST'])
def api_users_sign_in():
    return get_user(request)


@app.route('/api/users/sign-up', methods=['POST'])
def api_users_sign_up():
    return post_user(request)


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
