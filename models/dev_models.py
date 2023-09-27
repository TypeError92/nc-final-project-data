from db.pool import pool


def fetch_num_of_connections():
    connection = pool.getconn()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT count(*)
        FROM pg_stat_activity;
        """
    )
    open_connections = cursor.fetchall()
    connection.close()
    pool.putconn(connection)
    return open_connections

print(fetch_num_of_connections())
