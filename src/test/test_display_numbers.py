import unittest
import sys, os
import mysql.connector
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import display_numbers

class test_display_numbers(unittest.TestCase):
    """Unit tests for display_numbers.py file."""
    
    def test_is_file_display_numbers(self):
        """Checks if the 'display_numbers.py' file exists."""
        res = os.path.isfile("src\display_numbers.py")
        exp = True
        self.assertEqual(res, exp)


    def test_connect(self):
        """Test the connection."""
        conn, cursor = display_numbers.connect()
        res = conn
        exp = mysql.connector.connection_cext.CMySQLConnection
        self.assertIsInstance(res, exp)
        
        res = cursor
        exp = mysql.connector.cursor_cext.CMySQLCursorPrepared
        self.assertIsInstance(res, exp)


    def test_user_location(self):
        """Testing."""
        res = display_numbers.user_location()
        self.assertTrue(res)
        
    
    def test_helpline_phone_numbers_headings(self):
        """Testing if we get numberes and headings."""
        res = display_numbers.helpline_phone_numbers_headings()
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
