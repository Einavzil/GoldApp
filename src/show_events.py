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
        conn =  mysql.connector.connect(**dsn)
        cursor = conn.cursor(prepared=True)
        return conn, cursor
    except Exception as err:
        print(err)


def user_location():
    """User location based on the email id they are signed in with.
    Shown in the area 'Local Events and Meetups: ...'.
    """
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

        # hard coded at the moment!!!!
        args = ("example@gmail.com",)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result[0])
        return result[0]            # The location

    except Exception as err:
        print(err)


def user_interest():
    try:
        conn, cursor = connect()
        sql = """
            SELECT i.interest
            FROM goldapp.interest AS i
            JOIN goldapp.user_has_interest AS ints
            ON i.interest_id = ints.interest_interest_id
            JOIN goldapp.user AS u
            ON ints.user_email = u.email
            and email = ?
            ;
            """

        # hard coded at the moment!!!!
        args = ("example@gmail.com",)
        cursor.execute(sql, args)
        result = cursor.fetchall()
        interest_list = []
        for res in result:
            interest_list.append(res[0])
        cursor.close()
        conn.close()
        print(interest_list)
        return interest_list        # List of user interest

    except Exception as err:
        print(err)

def nr_of_events_to_display():
    """The total number of events that could be displayed to that user.
    Based on that could be 'loaded the events windows.'
    """
    try:
        conn, cursor = connect()
        sql = """
            SELECT count(goldapp.event.name)
            FROM goldapp.event
            JOIN goldapp.interest
            ON goldapp.event.interest_interest_id = interest.interest_id
            JOIN goldapp.user_has_interest
            ON goldapp.interest.interest_id = user_has_interest.interest_interest_id
            JOIN goldapp.user
            ON goldapp.user_has_interest.user_email = goldapp.user.email
            JOIN goldapp.location
            ON goldapp.user.location_location_id = location.location_id
            WHERE location.place = goldapp.event.city
            and email = ?
            ;
            """

        # hard coded at the moment!!!!
        args = ("example@gmail.com",)
        cursor.execute(sql, args)
        nr_of_events = cursor.fetchone()
        print(nr_of_events[0])
        
        cursor.close()
        conn.close()
        return nr_of_events[0]

    except Exception as err:
        print(err)


def events_in_location():
    """List of events based on user location and interests."""
    try:
        conn, cursor = connect()
        sql = """
            SELECT goldapp.event.name,
	        event.eventdate,
            event.eventtime,
	        event.address_line,
            event.city,
            interest.interest,
            interest.image_path,
	        event.information
            FROM goldapp.event
            JOIN goldapp.interest
            ON goldapp.event.interest_interest_id = interest.interest_id
            JOIN goldapp.user_has_interest
            ON goldapp.interest.interest_id = user_has_interest.interest_interest_id
            JOIN goldapp.user
            ON goldapp.user_has_interest.user_email = goldapp.user.email
            JOIN goldapp.location
            ON goldapp.user.location_location_id = location.location_id
            WHERE location.place = goldapp.event.city
            and email = ?
            ;
            """
        # hard coded at the moment!!!!
        args = ("example@gmail.com",)
        cursor.execute(sql, args)
        event_name, date, time, address, city, interest, image, desc = cursor.fetchone()
        print(event_name)
        print(date)
        print(time)
        print(address)
        print(city)
        print(interest)
        print(image)
        print(desc)
        # res = cursor.fetchall()
        # for i in res:
        #     print(i)
        
        cursor.close()
        conn.close()
        return event_name, date, time, address, city, interest, image, desc

    except Exception as err:
        print(err)
    


if __name__ == "__main__":
    user_location()
    user_interest()
    nr_of_events_to_display()
    events_in_location()