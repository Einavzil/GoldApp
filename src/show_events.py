from re import U
import json
import mysql.connector

import sys

sys.path.insert(0, "../src")
# import login


def connect():
    dsn = {
        "user": "maria",
        "password": "password",
        "host": "localhost",
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
    """User location based on the email id they are signed in with."""
    try:
        conn, cursor = connect()
        sql = """
            SELECT
                goldapp.location.place
            FROM
	            goldapp.user,
	            goldapp.location
            WHERE
	            location.location_id = user.location_location_id
                and email = ?
            ;
            """
        # fetching logged in user from the text file
        try:
            with open("current_email.txt", "r") as current_email:
                email = current_email.readline()
        except:
            with open("src\current_email.txt", "r") as current_email:
                email = current_email.readline()
        args = (email,)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        # print(result[0])
        return result[0]  # The location

    except Exception as err:
        print(err)


def events_details(events_id):
    """This function will fetch all events from the database
    based on the id's received.
    """
    id_tuple = tuple(events_id)
    try:
        conn, cursor = connect()
        sql = f"""
        SELECT JSON_OBJECT(
            'name', event.name,
            'event_date', event.eventdate,
            'event_time', event.eventtime,
            'address', event.address_line,
            'city', event.city,
            'interest', interest.interest,
            'image_path', interest.image_path,
            'information', event.information)
        FROM event, interest
        WHERE event.interest_interest_id = interest.interest_id
        AND event.event_id IN {id_tuple}
        ;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    except Exception as err:
        print(err)


def event_ids_list():
    """This function will get the id's of the events that need to be displayed."""
    try:
        conn, cursor = connect()
        sql = """
            SELECT event_id
            FROM event
            JOIN user
            ON user.location_location_id = event.location_id
            JOIN user_has_interest
            ON user.email = user_has_interest.user_email
            AND event.interest_interest_id = user_has_interest.interest_interest_id
            WHERE user.email = ?
            ;
            """
        # fetching logged in user from the text file
        try:
            with open("current_email.txt", "r") as current_email:
                email = current_email.readline()
        except:
            with open("src\current_email.txt", "r") as current_email:
                email = current_email.readline()

        args = (email,)
        cursor.execute(sql, args)
        event_id = cursor.fetchall()
        events = []
        for i in event_id:
            events.append(i[0])
        # print(events)
        cursor.close()
        conn.close()
        return events

    except Exception as err:
        print(err)


def show_events():
    """Call this function to get all the events in list of tuples."""
    event_list = event_ids_list()
    return event_list, events_details(event_list)


if __name__ == "__main__":
    # print(show_events())
    show_events()