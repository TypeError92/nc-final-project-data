endpoints = {
  "GET /api/": {
    "description": "serves up a json representation of all available endpoints"
  },
  "GET /api/questions/random/": {
    "description": "serves up a random question",
    "queries": ["category_name", "number", "game_id"],
    "example_response": [
        {"question": "IN ATTIC", "answer": "TITANIC", "category": "movie"},
        {"question": "CORKY", "answer": "ROCKY", "category": "movie"},
        {"question": "NOT PUT", "answer": "TOP GUN", "category": "movie"}
    ]
  },
  "POST /api/users": {
    "description": "creates a new user and serves up a the new user object"
  },
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