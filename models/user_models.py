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
    user_id, username, avatar_url, high_score, lifetime_score = cursor.fetchall()[0]
    connection.commit()
    connection.close()
    pool.putconn(connection)
    return {
        'user_id': user_id,
        'username': username,
        'avatar_url': avatar_url,
        'high_score': high_score,
        'lifetime_score': lifetime_score
    }

def fetch_users(order_by):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
                SELECT * FROM users
                ORDER BY {order_by} DESC;
                """,
    )
    user_rows = cursor.fetchall()
    connection.commit()
    connection.close()
    pool.putconn(connection)
    users = []
    for (user_id, username, avatar_url, high_score, lifetime_score) in user_rows:
        users.append({
        'user_id': user_id,
        'username': username,
        'avatar_url': avatar_url,
        'high_score': high_score,
        'lifetime_score': lifetime_score
    })
    return users


def insert_user(user_id, username, avatar_url):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
            INSERT INTO users (
                user_id, username, avatar_url
            )
            VALUES (%s, %s, %s);
            """,
        (user_id, username, avatar_url)
    )
    connection.commit()
    connection.close()
    pool.putconn(connection)
    return {
        'user_id': user_id,
        'username': username,
        'avatar_url': avatar_url
    }


def update_high_score(user_id, score):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
            UPDATE users
            SET high_score = {score}
            WHERE user_id = '{user_id}';
            """
)
    # Update lifetime score
    connection.commit()
    connection.close()
    pool.putconn(connection)
    return

def update_lifetime_score(user_id, score):
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        f"""
            UPDATE users
            SET lifetime_score = lifetime_score + {score}
            WHERE user_id = '{user_id}'
            RETURNING lifetime_score;
        """
    )
    new_lifetime_score = cursor.fetchall()[0]
    # Update lifetime score
    connection.commit()
    connection.close()
    pool.putconn(connection)
    return new_lifetime_score