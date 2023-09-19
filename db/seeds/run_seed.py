from db.connect import connect
from db.data.dev_data.answers import answers
from db.data.dev_data.categories import categories
from db.data.dev_data.users import users
from seed import seed

connection = connect('dev')

seed(connection, answers, categories)