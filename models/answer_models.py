from db.pool import pool
from random import sample


def fetch_answers():
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT answer
        FROM answers;
        """
    )
    answers = cursor.fetchall()
    connection.close()
    pool.putconn(connection)
    return sample(answers, k=9)
