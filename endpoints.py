endpoints = {

    # /API

    "GET /api": {
        "description": "serves up a json representation of all available endpoints",
        "access": "any",
        "queries": {}
    },

    # /API/LEADERBOARD

    "GET /api/leaderboard": {
        "access": "any",
        "description": "serves up an array representation of the current leaderboard",
        "queries": {"limit": {"description": "number of entries to be returned;"
                                             "if omitted, the entire leaderboard will be returned",
                              "type": "integer",
                              "default": None},
                    "page": {"description": "page of leaderboard to be returned;"
                                            "will only be considered in combination with a 'limit' query",
                             "type": "integer",
                             "default": 1}},
        "example_response": {"entries": [
            {"rank": 1, "username": "phil", "score": 1234},
            {"rank": 2, "username": "charlotte", "score": 1111},
            {"rank": 3, "username": "chris", "score": 999}
        ]}
    },

    "PATCH /api/leaderboard": {
        "access": "admin",
        "description": "submits player scores to update leaderbo",
        "queries": {"limit": {"description": "number of entries to be returned;"
                                             "if omitted, the entire leaderboard will be returned",
                              "type": "integer",
                              "default": None},
                    "page": {"description": "page of leaderboard to be returned;"
                                            "will only be considered in combination with a 'limit' query",
                             "type": "integer",
                             "default": 1}},
        "example_response": {"entries": [
                {"rank": 1, "username": "phil", "score": 1234},
                {"rank": 2, "username": "charlotte", "score": 1111},
                {"rank": 3, "username": "chris", "score": 999}
            ]}
    },
    "GET /api/questions/": {
        "description": "serves up a list of question/answer pairs",
        "queries": ["category_name", "number", "game_id"],
        "example_response": {
            "questions": [
                {"question": "IN ATTIC", "answer": "TITANIC", "category": "movie"},
                {"question": "CORKY", "answer": "ROCKY", "category": "movie"},
                {"question": "NOT PUT", "answer": "TOP GUN", "category": "movie"}
            ]
        }
    },
    "POST /api/users": {
        "description": "creates a new user and serves up a the new user object",
        "access": "admin",
        "queries": {},
        "example_request": {"username": "punny bunny"},
        "example_response": {"username": "punny bunny"}

    },

    # /api/users/username
    "GET /api/users/username": {
        "description": "returns an existing user"
    },
    "PATCH /api/users/username": {
        "description": "patches an existing user"
    },
    "DELETE /api/users/username": {
        "description": "deletes a user"
    }
}
