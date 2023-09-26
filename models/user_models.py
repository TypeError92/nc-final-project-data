from db.pool import pool


def fetch_user(user_id):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
            SELECT * FROM users
            WHERE user_id='{user_id}';
            """,
    )
    user_id, username, avatar_id = cursor.fetchall()[0]
    connection.commit()
    connection.close()
    pool.putconn(connection)
    return {
        'user_id': user_id,
        'username': username,
        'avatar_id': avatar_id
    }


def insert_user(user_id, username, avatar_id):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
            INSERT INTO users (
                user_id, username, avatar_id
            )
            VALUES (%s, %s, %s);
            """,
        (user_id, username, avatar_id)
    )
    connection.commit()
    connection.close()
    pool.putconn(connection)
    return {
        'user_id': user_id,
        'username': username,
        'avatar_id': avatar_id
    }