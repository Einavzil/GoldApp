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
        """Tests the connection."""
        res = show_events.connect()
        exp = True
        self.assertTrue(res, exp)

    def test_user_location(self):
        """Location."""
        user_email = 'example@gmail.com'
        exp = show_events.user_location()
        res = user_email
        self.assertTrue(res, exp)
        
        
        
        
    def test_event_details(self):
        """Event details."""
        


    def test_event_ids_list(self):
        """Event List."""
        


    def test_show_events(self):
        """Show events."""
        exp = show_events.show_events()
        res = show_events.show_events()
        self.assertEqual(exp, res)

if __name__ == "__main__":
    unittest.main()
