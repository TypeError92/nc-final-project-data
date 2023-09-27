import psycopg2.errors
from db.pool import pool
from random import sample


def fetch_questions():
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT question, questions.answer, category, subcategory
        FROM questions
        JOIN answers
        ON questions.answer = answers.answer;
        """
    )
    questions = cursor.fetchall()
    connection.close()
    pool.putconn(connection)
    return sample(questions, k=9)


def insert_questions(questions: list[tuple[str, str], ...]):
    inserted_questions = []
    connection = pool.getconn()
    cursor = connection.cursor()
    for question in questions:
        try:
            cursor.execute(
                f"""
                INSERT INTO questions (
                    question, answer
                )
                VALUES (%s, %s);
                """,
                question
            )
            inserted_questions.append(question)
        except psycopg2.errors.UniqueViolation:
            print(f'"{question}" is a duplicate and will be ignored.')

    connection.close()
    pool.putconn(connection)
    return inserted_questions
