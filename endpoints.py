endpoints = {

    # /API

    "GET /api": {
        "description": "Serves up a json representation of all available endpoints.",
        "requires authentication": False,
        "queries": {}
    },

    # /API/QUESTIONS

    "GET /api/questions/": {
        "description": "serves up a list of 9 questions",
        "requires authentication": True,
        "queries" : {},
        "example response": [
            {'question': 'IODINE TOTEM', 'answer': 'NO TIME TO DIE'},
            {'question': 'HIGHEST INN', 'answer': 'THE SHINING'},
            {'question': 'BOTH BE HIT', 'answer': 'THE HOBBIT'},
            {'question': 'HE HIT BELLBOY', 'answer': 'THE HOLY BIBLE'},
            {'question': 'IN DRAMA KHAKIS', 'answer': 'KIM KARDASHIAN'},
            {'question': 'AM A BACK BOAR', 'answer': 'BARACK OBAMA'},
            {'question': 'CORSICA NYMPHAE', 'answer': 'AMERICAN PSYCHO'},
            {'question': 'TEEN HELL RIO', 'answer': 'ONE TREE HILL'},
            {'question': 'GENT SHEW WIT', 'answer': 'THE WEST WING'}
        ]
    },

    # /API/STATS

    "GET /api/stats/num-of-connections": {
        "description": "serves up the current number of open connections to the database",
        "requires authentication": True,
        "queries": {},
        "example response": 139
    },

    # /API/USERS

    "GET /api/users": {
        "description": "serves up a list of all existing users",
        "requires authentication": True,
        "queries": {
            "order_by": {
                "required": False,
                "options": [
                    "user_id",
                    "username",
                    "avatar_url",
                    "high_score",
                    "lifetime_score"
                ],
                "default": "user_id"
            }
        },
        "example response": [
            {
                "user_id": "provided_by_firebase",
                "username": "punny bunny",
                "avatar_url": "profile/pic/path"
            },
            {
                "user_id": "also_provided_by_firebase",
                "username": "sunny honey",
                "avatar_url": "other/profile/pic/path"
            }
        ]
    },

    "POST /api/users/new-score": {
        "description": "posts a user's latest score to the database and updates high score if appropriate",
        "requires authentication": True,
        "queries": {},
        "example request": {
            "user_id": "provided_by_firebase",
            "score": 2222
        },
        "example response": {
            "user_id": "3",
            "new_high_score": True,
            "new_lifetime_score": 8888,
            "score": 2222},
    },

    "POST /api/users/sign-up": {
        "description": "adds a new user to the database and serves up a the new user object",
        "requires authentication": True,
        "queries": {},
        "example request": {
            "user_id": "provided_by_firebase",
            "username": "punny bunny",
            "avatar_url": "profile/pic/path"
        },
        "example response": {
            "user_id": "provided_by_firebase",
            "username": "punny bunny",
            "avatar_url": "profile/pic/path"
        }
    },

    "POST /api/users/sign-in": {
        "description": "serves up an existing user object matching the provided user_id",
        "requires authentication": True,
        "queries": {},
        "example request": {
            "user_id": "provided_by_firebase"
        },
        "example response": {
            "user_id": "provided_by_firebase",
            "username": "punny bunny",
            "avatar_url": "profile/pic/path"
        }
    }
}
