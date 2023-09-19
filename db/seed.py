from db.connect import connect
from importlib import import_module

def seed(env_name):
    # LOAD DATA
    answers = import_module(f'db.data.{env_name}.answers').answers
    categories = import_module(f'db.data.{env_name}.categories').categories
    questions = import_module(f'db.data.{env_name}.questions').questions

    # CONNECT TO DATABASE
    connection = connect(env_name)
    cursor = connection.cursor()
    query = cursor.execute


    # CATEGORIES

    query("""DROP TABLE IF EXISTS categories;""")
    query("""CREATE TABLE categories (
                name TEXT PRIMARY KEY,
                description TEXT);""")
    print('CREATED TABLE CATEGORIES')
    for category in categories:
        query(f"""INSERT INTO categories (name, description)
                    VALUES ('{category['name']}', '{category['description']}');""")

    # ANSWERS
    query("""DROP TABLE IF EXISTS answers;""")

    # ANSWERS_CATEGORIES
    query("""DROP TABLE IF EXISTS answers_categories;""")

    # QUESTIONS
    query("""DROP TABLE IF EXISTS questions;""")


    # FINALISE
    connection.commit()
    connection.close()

