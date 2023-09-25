import os
from importlib import import_module
from db.pool import pool


def seed():
    env_name = os.getenv('PYTHON_ENV')
    print(f'Seeding @{env_name}')
    # LOAD DATA
    answers = import_module(f'db.data.{env_name}.answers').answers
    questions = import_module(f'db.data.{env_name}.questions').questions

    # CONNECT TO DATABASE
    connection = pool.getconn()
    cursor = connection.cursor()
    query = cursor.execute

    # DROP EXISTING TABLES
    print('Dropping existing tables...')
    query("""DROP TABLE IF EXISTS questions;""")
    query("DROP TABLE IF EXISTS answers;")
    print('All tables dropped!')

    # SEED TABLE: ANSWERS
    print('Seeding answers...')
    query("CREATE TABLE answers ("
          "answer VARCHAR(50) PRIMARY KEY,"
          "category VARCHAR(20)"
          ");")

    for answer in answers:
        query(f"""INSERT INTO answers
              (answer, category)
              VALUES
              ('{answer['answer']}', '{answer['category']}');""")
    print('Answers seeded!')

    # SEED TABLE: QUESTIONS
    query("""
    CREATE TABLE questions (
        question VARCHAR(50) PRIMARY KEY,
        answer VARCHAR(50) REFERENCES answers
        );
    """)

    for question in questions:
        query(f"""INSERT INTO questions
              (question, answer)
              VALUES
              ('{question['question']}', '{question['answer']}');""")


    # FINALISE
    print(f'Committing changes @{env_name}')
    connection.commit()
    connection.close()

