import unittest
import sys, os
import mysql.connector
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import show_events


class test_show_events(unittest.TestCase):
    """Unit tests for show_events.py file."""
    
    def test_is_file_show_events(self):
        """Checks if the 'show_events.py' file exists."""
        res = os.path.isfile("src\show_events.py")
        exp = True
        self.assertEqual(res, exp)

   
    def test_connect(self):
        """Test the connection."""
        conn, cursor = show_events.connect()
        res = conn
        exp = mysql.connector.connection_cext.CMySQLConnection
        self.assertIsInstance(res, exp)
        
        res = cursor
        exp = mysql.connector.cursor_cext.CMySQLCursorPrepared
        self.assertIsInstance(res, exp)     


    def test_user_location(self):
        """Location. Dependent on the example email."""
        with open("src\current_email.txt", "r") as current_email:
            email = current_email.readline()
            email2 = email
        if email == 'example@gmail.com':
            res = show_events.user_location()
            exp = "Stockholm"
            self.assertEqual(res, exp)
        elif email == 'liis@gmail.com':
            res = show_events.user_location()
            exp = "Stockholm"
            self.assertEqual(res, exp)


    def test_is_file_current_email(self):
        """Checks if the 'current_email.txt' file exists."""
        res = os.path.isfile("src\current_email.txt")
        exp = True
        self.assertEqual(res, exp)


    def test_events_details(self):
        """Event details. Can we get 2 back."""
        eve = (1,2)
        deets = show_events.events_details(eve)
        res = len(deets)
        exp = 2
        self.assertEqual(res, exp)


    def test_event_ids_list(self):
        """Event List."""
        res = show_events.event_ids_list()
        exp = list
        self.assertIsInstance(res, exp)
        
        id_s, deets = show_events.show_events()
        exp = id_s
        self.assertEqual(res, exp)
        
        

    def test_show_events(self):
        """Show events. Nr of events/event-ids."""
        number_list, event_deets = show_events.show_events()
        print(number_list)
        print(event_deets)
        if event_deets != None:
            self.assertEqual(len(number_list), len(event_deets))

        res = number_list
        exp = show_events.event_ids_list()
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
