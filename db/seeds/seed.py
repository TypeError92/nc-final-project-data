def seed(connection, categories, answers, users):
    cursor = connection.cursor()
    query = cursor.execute

    # CATEGORIES

    query("""DROP TABLE IF EXISTS categories;""")
    query("""CREATE TABLE categories (
                category_id SERIAL PRIMARY KEY,
                category_name TEXT,
                category_description TEXT);""")
    for category in categories:
        query(f"""INSERT INTO categories (category_name, category_description)
                    VALUES ('{category['category_name']}', '{category['category_description']}');""")

    # ANSWERS

    for answer in answers:
        pass

    # USERS

    for user in users:
        pass

    connection.commit()
    connection.close()

