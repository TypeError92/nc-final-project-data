from db.dev_pool import pool

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
