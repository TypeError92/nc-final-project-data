import psycopg2.errors
from db.pool import pool

def fetch_questions():
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT question, answer, category
        FROM questions
        JOIN answers
        ON questions.answer_id = answers.answer_id
        LIMIT 9;
        """
    )
    questions = cursor.fetchall()
    connection.close()
    pool.putconn(connection)
    return questions


def insert_questions(questions):
    connection = pool.getconn()
    cursor = connection.cursor()
    for (question, answer) in questions:
        try:
            cursor.execute(
                """
                SELECT question, answer, category
                FROM questions
                JOIN answers
                ON questions.answer_id = answers.answer_id
                LIMIT 9;
                """
            )
        except psycopg2.errors.UniqueViolation:
            print(f'"{question}" is a duplicate and will be ignored.')

    connection.close()
    pool.putconn(connection)
