import auth
from endpoints import endpoints
from flask import Flask, make_response, request

app = Flask(__name__)


# TODO: Add all endpoints here.

@app.route('/api/')
@auth.admin
def api():
    return endpoints


@app.route('/api/questions/')
@auth.admin
def api_questions():
    return make_response(
        {"questions": [
            {"question": "IN ATTIC", "answer": "TITANIC", "category": "movie"},
            {"question": "CORKY", "answer": "ROCKY", "category": "movie"},
            {"question": "NOT PUT", "answer": "TOP GUN", "category": "movie"}]
        },
        200)


@app.route('/api/users', methods=['POST'])
@auth.admin
def api_users():
    pass


@app.route('/api/users/<username>', methods=['GET', 'PATCH', 'DELETE'])
@auth.user
def api_users__username(username):
    if request.method == 'GET':
        return make_response({"user": {"username": username}}, 200)
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass


if __name__ == '__main__':
    app.run()
