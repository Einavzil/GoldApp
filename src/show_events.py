import mysql.connector

# import sys
# sys.path.insert(0, "../src")
# import login


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


def events_ids(events_id):
    """This function will fetch all events from the database
    based on the id's received.
    """
    id_tuple = tuple(events_id)
    try:
        conn, cursor = connect()
        sql = f"""
        SELECT
            event.name,
            event.eventdate,
            event.eventtime,
            event.address_line,
            event.city,
            interest.interest,
            interest.image_path,
            event.information
        FROM event, interest
        WHERE event.interest_interest_id = interest.interest_id
        AND event.event_id IN {id_tuple}
        ;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        # print(result)
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
        with open("src/current_email.txt", "r") as current_email:
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
    print(events_ids(event_ids_list()))
    return events_ids(event_ids_list())


if __name__ == "__main__":
    show_events()