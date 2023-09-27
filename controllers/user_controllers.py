from models import fetch_user, insert_user, update_high_score, update_lifetime_score


def get_user(req):
    body = req.get_json()
    return fetch_user(body['user_id'])


def patch_scores(req):
    body = req.get_json()
    user_id, score = body['user_id'], body['score']
    user = get_user(user_id)
    if score > user['high_score']:
        new_high_score = True
        update_high_score(user_id, score)
    else:
        new_high_score = False
    new_lifetime_score = update_lifetime_score(user_id, score)
    return {'user_id': user_id, 'score': score, 'new_high_score': new_high_score, 'new_lifetime_score': new_lifetime_score}


def post_user(req):
    body = req.get_json()
    return insert_user(body['user_id'], body['username'], body['avatar_url'])
