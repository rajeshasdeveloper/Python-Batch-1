import sqlite3


def db_servie(query):
    sqliteConnection = sqlite3.connect("sql.db")
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    sqliteConnection.commit()
    result = cursor.fetchall()
    print(result)
    return result


# db_servie(
#     """
#     INSERT INTO USERS (USER_ID, USER_NAME) VALUES (2, 'JAVA')
#     """
# )

# db_servie("select * from users")
