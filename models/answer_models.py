from db.pool import pool


def fetch_answers():
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT answer
        FROM answers
        LIMIT 9;
        """
    )
    questions = cursor.fetchall()
    connection.close()
    pool.putconn(connection)
    return questions
