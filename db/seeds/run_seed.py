from db.connect import connect
from db.data.dev_data.answers import answers
from db.data.dev_data.categories import categories
from db.data.dev_data.users import users
from db.data.dev_data.questions import questions
from seed import seed

connection = connect('dev')

seed(connection, categories, answers, questions, users)
