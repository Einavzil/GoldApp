"""Connecting to database."""

import mysql.connector

dsn = {
    "user": "maria",
    "password": "pass",
    "host": "127.0.0.1",
    "port": "3306",
    "database": "goldapp",
    "raise_on_warnings": True,
}
print("connection test")
print(dsn)
