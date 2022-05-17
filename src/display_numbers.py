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


def user_location():
    """logged in user location."""
    return show_events.user_location()


def helpline_phone_numbers_headings():
    """Numbers and heading in that location."""
    location = user_location()
    conn, cursor = connect()

    sql = """
        SELECT phone, heading
        FROM info
        JOIN location_has_info
        ON info.info_id = location_has_info.info_info_id
        JOIN location
        ON location_has_info.location_location_id = location.location_id
        AND place = ?
        ;
        """
    args = (location,)
    cursor.execute(sql, args)
    helpline_info = cursor.fetchall()
    if helpline_info == None:
        return ""
    return helpline_info
    
    
print(user_location())
print(helpline_phone_numbers_headings())
