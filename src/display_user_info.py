import mysql.connector
import sys
import show_events
sys.path.insert(0, "../src")


def connect():
    """Database connection."""
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


def user_email():
    """Email the user logged in with."""
    try:
        with open("src/current_email.txt", "r") as email_file:
            email = email_file.readline()
    except:
        with open("src/current_email.txt", "r") as email_file:
            email = email_file.readline()
    return email


def user_first_name():
    conn, cursor = connect()
    email = user_email()

    sql = """
        SELECT fname
        FROM goldapp.user 
        where email = ?
        ;
        """
    args = (email,)
    cursor.execute(sql, args)
    first_name = cursor.fetchone()
    if first_name == None:
        return ""
    return first_name[0]
    
    
def user_last_name():
    """Last name on the user."""
    conn, cursor = connect()
    email = user_email()

    sql = """
        SELECT lname
        FROM goldapp.user 
        where email = ?
        ;
        """
    args = (email,)
    cursor.execute(sql, args)
    last_name = cursor.fetchone()
    if last_name == None:
        return ""
    return last_name[0]


def user_phone():
    """What is the registered number."""
    conn, cursor = connect()
    email = user_email()

    sql = """
        SELECT phone
        FROM goldapp.user 
        where email = ?
        ;
        """
    args = (email,)
    cursor.execute(sql, args)
    phone = cursor.fetchone()
    return phone[0]
    

def user_location():
    """logged in user location."""
    return show_events.user_location()
