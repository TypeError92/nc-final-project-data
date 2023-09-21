from db.connect import pool
from importlib import import_module

def seed(env_name):
    print(f'Seeding @{env_name}')
    # LOAD DATA
    answers = import_module(f'db.data.{env_name}.answers').answers
    questions = import_module(f'db.data.{env_name}.questions').questions

    # CONNECT TO DATABASE
    connection = pool(env_name).getconn()
    cursor = connection.cursor()
    query = cursor.execute

    # DROP EXISTING TABLES
    query("""DROP TABLE IF EXISTS questions;""")
    query("DROP TABLE IF EXISTS answers;")

    # SEED TABLE: ANSWERS

    query("CREATE TABLE answers ("
          "answer_id SERIAL PRIMARY KEY,"
          "answer VARCHAR(50),"
          "category VARCHAR(20)"
          ");")

    for answer in answers:
        query(f"""INSERT INTO answers
              (answer, category)
              VALUES
              ('{answer['answer']}', '{answer['category']}');""")



    # SEED TABLE: QUESTIONS
    query("""
    CREATE TABLE questions (
        question_id SERIAL PRIMARY KEY,
        question VARCHAR(50),
        answer_id INT REFERENCES answers
        );
    """)

    for question in questions:
        query(f"""INSERT INTO questions
              (question, answer_id)
              VALUES
              ('{question['question']}', '{question['answer_id']}');""")


    # FINALISE
    print(f'Committing changes @{env_name}')
    connection.commit()
    connection.close()

