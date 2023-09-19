endpoints = {
  "GET /api/help": {
    "description": "serves up a json representation of all available endpoints"
  },
  "GET /api/questions/random/": {
    "description": "serves up a random question",
    "queries": ["category_name", "game_id"],
    "example_response": {

    }
  },

}