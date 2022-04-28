import mysql.connector

def connect():
    dsn = {
        "user": "maria",
        "password": "password",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "goldapp",
        "raise_on_warnings": True,
        }
    try:
        conn =  mysql.connector.connect(**dsn)
        cursor = conn.cursor(prepared=True)
        return conn, cursor
    except Exception as err:
        print(err)