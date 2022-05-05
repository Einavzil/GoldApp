import unittest
import json
import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import show_events


class TestShowEvents(unittest.TestCase):
    """Unittest."""
   
    def test_connect(self):
        """Test the connection."""
        connection = show_events.connect()
        if connection == None:
            self.assertFalse(connection)
            self.assertRaises(Exception)
        else:
            self.assertTrue(connection)


    def test_user_location(self):
        """Location."""
        with open("src\current_email.txt", "r") as current_email:
            email = current_email.readline()
        if email == 'example@gmail.com':
            res = show_events.user_location()
            exp = "Stockholm"
            self.assertEqual(res, exp)
        elif email == 'liis@gmail.com':
            res = show_events.user_location()
            exp = "Stockholm"
            self.assertEqual(res, exp)


    def test_events_details(self):
        """Event details."""
        eve = (1,2)
        deets = show_events.events_details(eve)
        res = len(deets)
        exp = 2
        self.assertEqual(res, exp)
        
        res = len(show_events.event_ids_list())
        exp = len(show_events.events_details(show_events.event_ids_list()))
        self.assertEqual(res, exp)


    def test_event_ids_list(self):
        """Event List."""
        res = show_events.event_ids_list()
        exp = list
        self.assertIsInstance(res, exp)
        

    def test_show_events(self):
        """Show events.Nr of events/event-ids."""
        e, q = show_events.show_events()
        self.assertEqual(len(e), len(q))


if __name__ == "__main__":
    unittest.main()
