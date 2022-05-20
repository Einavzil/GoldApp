import unittest
import sys, os
import mysql.connector
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import help_page_conn

class test_help_page_conn(unittest.TestCase):
    """Unit tests for help_page_conn.py file."""
    
    def test_is_file_help_page_conn(self):
        """Checks if the 'help_page_conn.py' file exists."""
        res = os.path.isfile("src\help_page_conn.py")
        exp = True
        self.assertEqual(res, exp)


    def test_connect(self):
        """Test the connection."""
        conn, cursor = help_page_conn.connect()
        res = conn
        exp = mysql.connector.connection_cext.CMySQLConnection
        self.assertIsInstance(res, exp)
        
        res = cursor
        exp = mysql.connector.cursor_cext.CMySQLCursorPrepared
        self.assertIsInstance(res, exp)


    def test_user_email(self):
        """Checking if we get the correct email."""
        with open("src/current_email.txt", "r") as email_file:
            email = email_file.readline()
        res = help_page_conn.user_email()
        exp = email
        self.assertEqual(res, exp)
        

    def test_user_first_name(self):
        """Testing, if we get the firt name."""
        res = help_page_conn.user_first_name()
        self.assertTrue(res)


    def test_user_last_name(self):
        """Testing, if we get the last name."""
        res = help_page_conn.user_last_name()
        self.assertTrue(res)

   
    def test_user_phone(self):
        """Testing, if we get the user phone."""
        res = help_page_conn.user_phone()
        self.assertTrue(res)


    def test_insert_form(self):
        """Testing values."""
        res = help_page_conn.insert_form("liis@gmail.com", "health", "hehe")
        self.assertTrue(res)

    def test_user_location(self):
        """Testing if we geet the user location."""
        res = help_page_conn.user_location()
        self.assertTrue(res)
        
        
if __name__ == "__main__":
    unittest.main()
