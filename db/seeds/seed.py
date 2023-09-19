def seed(connection, answers, categories):
    cursor = connection.cursor()
    query = cursor.execute
    query("""DROP TABLE IF EXISTS categories;""")
    query("""CREATE TABLE categories (
                category_name TEXT PRIMARY KEY,
                category_description TEXT);""")
    for category in categories:
        query = f"""INSERT INTO categories (category_name, category_description)
                    VALUES ("{category['category_name']}", "{category['category_description']}");"""
        print(query)
    connection.commit()
    connection.close()

