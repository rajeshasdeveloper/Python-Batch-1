import sqlite3, os


def db_servie(query, params=[]):
    try:
        sqliteConnection = sqlite3.connect("sql.db")
        cursor = sqliteConnection.cursor()
        cursor.execute(query, params)
        sqliteConnection.commit()
        result = cursor.lastrowid
        return result
    except Exception as err:
        return str(err)


def validate_database():
    query_file = os.getcwd() + "/sql/user/tables.sql"
    with open(query_file, "r") as sql_queries:
        for query in sql_queries.readlines():
            db_servie(query)
