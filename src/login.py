import mysql.connector
from cryptography.fernet import Fernet
import sys

sys.path.insert(0, "../src")


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
        conn = mysql.connector.connect(**dsn)
        cursor = conn.cursor(prepared=True)
        return conn, cursor
    except Exception as err:
        print(err)


def check_email(email):
    try:
        conn, cursor = connect()

        sql = """
            SELECT
            email
            FROM user
            WHERE email = ?
            ;
            """

        args = (email,)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result[0] == email:
            return True
        return False

    except Exception as err:
        print(err)


def check_password(email, password):
    try:
        conn, cursor = connect()

        sql = """
            SELECT
            pwd
            FROM user
            WHERE email = ?
            ;
            """

        args = (email,)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        # cursor.close()
        # conn.close()

        decrepted_pass = decrypt_pass(result[0])
        if decrepted_pass == password:
            return True
        return False

    except Exception as err:
        print(err)


def decrypt_pass(password):
    """Key is opened from 'enc_key.bin' file."""
    print(sys.path)
    try:
        with open("src\enc_key.bin", "rb") as key_file:
            key = key_file.readline()
    except:
        with open("enc_key.bin", "rb") as key_file:
            key = key_file.readline()

    fernet = Fernet(key)
    """decrypting the password into string and return it."""
    decr_pass = fernet.decrypt(password.encode())

    return decr_pass.decode()


def store_current_email(email):
    try:
        with open("current_email.txt", "w") as login_file:
            login_file.write(email)
    except:
        with open("src\current_email.txt", "w") as login_file:
            login_file.write(email)


if __name__ == "__main__":
    print(check_email("example@gmail.com"))
    if check_email("example@gmail.com"):
        print(check_password("example@gmail.com", "abc123"))

    store_current_email("example@gmail.com")
