from db.connect import connect
from db.data.dev.answers import answers
from db.data.dev.categories import categories
from db.data.dev.users import users
from db.data.dev.questions import questions
from seed import seed

def run_seed(env_name):
    connection = connect(env_name)
    seed(connection, categories, answers, questions, users)
