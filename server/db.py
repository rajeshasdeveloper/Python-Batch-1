import sqlite3, os, mysql.connector

sqliteConnection = None


def connect_to_db(db_type):
    connection = ""
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "blueeyes",
        "database": "transactionserv",
    }
    if db_type == "mysql":
        connection = mysql.connector.connect(**db_config)
    else:
        connection = sqlite3.connect("sql.db")
    return connection


def db_service(query, params=[]):
    try:
        sqliteConnection = connect_to_db(os.getenv("DB_TYPE"))
        if sqliteConnection:
            cursor = sqliteConnection.cursor()
            cursor.execute(query, params)
            sqliteConnection.commit()
            return cursor
        else:
            return False
    except Exception as err:
        return {
            "error": str(err),
        }


def validate_database():
    query_file = os.getcwd() + "/sql/user/tables.sql"
    with open(query_file, "r") as sql_queries:
        for query in sql_queries.readlines():
            db_service(query)
