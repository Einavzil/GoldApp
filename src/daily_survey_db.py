import mysql.connector
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


def insert_data(answer1, answer2, answer3, answer4):
    try:
        print(answer4)
        conn, cursor = connect()

        sql = """
        INSERT INTO daily_survey (user_email, date, answer_1, answer_2, answer_3, free_text)
        VALUES (?, CURDATE(), ?, ?, ?, ?)
        ;
        """
        try:
            with open("current_email.txt", "r") as current_email:
                email = current_email.readline()
        except:
            with open("src\current_email.txt", "r") as current_email:
                email = current_email.readline()

        args = (email, answer1, answer2, answer3, answer4)
        cursor.execute(sql, args)
        conn.commit()

        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        return rowcount
    except Exception as err:
        print(err)

def check_last_survey():
    try:
        try:
            with open("current_email.txt", "r") as email_file:
                email = email_file.readline()
        except:
            with open("src/current_email.txt", "r") as email_file:
                email = email_file.readline()
                
        conn, cursor = connect()
        
        sql = """
        SELECT MAX(date), CURDATE()
        FROM daily_survey
        WHERE user_email = ?
        """

        args = (email,)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        
        if result[0] == result[1]:
            print(False)
            return False
        print(True)
        return True
    except Exception as err:
        print(err)
        