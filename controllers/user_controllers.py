from models import fetch_user, insert_user


def get_user(req):
    body = req.get_json()
    return fetch_user(body['user_id'])


def post_user(req):
    body = req.get_json()
    return insert_user(body['user_id'], body['username'], body['avatar_url'])

