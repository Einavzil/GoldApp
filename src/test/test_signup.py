import unittest
import os.path, sys
import mysql.connector
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import signup, login
import time


class test_signup(unittest.TestCase):
    """Unit tests for signup.py file."""
    
    def test_is_file_signup(self):
        """Checks if the 'signup.py' file exists."""
        res = os.path.isfile("src\signup.py")
        exp = True
        self.assertEqual(res, exp)


    def test_connect(self):
        """Test the connection."""
        conn, cursor = signup.connect()
        res = conn
        exp = mysql.connector.connection_cext.CMySQLConnection
        self.assertIsInstance(res, exp)
        
        res = cursor
        exp = mysql.connector.cursor_cext.CMySQLCursorPrepared
        self.assertIsInstance(res, exp)     


    def test_insert_account(self):
        """Testing if we can call the sign up with new data."""
        res = signup.insert_account
        self.assertTrue(res)
        
        milliseconds = int(round(time.time()))
        pwd = "pwd123"
        phone = int(milliseconds/9+milliseconds/9)
        loc = "Stockholm"
        
        """Can't sign up with existing email."""
        email = "liis@gmail.com"
        checking_email = login.check_email(email)
        if checking_email == True:
            res = signup.insert_account("test", "case", email, pwd, phone, loc)
            exp = None
            self.assertEqual(res, exp)
        

    def test_get_location_id(self):
        """Let's get the location id."""
        location = "Stockholm"
        res = signup.get_location_id(location)
        exp = 2
        self.assertEqual(res, exp)

        location = "Kristianstad"
        res = signup.get_location_id(location)
        exp = 1
        self.assertNotEqual(res, exp)


    def test_encrypt_pass(self):
        """Lets encrypt passwords."""
        passw = "password"
        res = signup.encrypt_pass(passw)
        exp = "password"
        self.assertIsNot(res, exp)
    

    def test_is_file_enc_key(self):
        """Checks if the 'enc_key.bin' file exists."""
        res = os.path.isfile("src\enc_key.bin")
        exp = True
        self.assertEqual(res, exp)
        

    def test_add_interest(self):
        """Test."""
        res = signup.add_interest
        self.assertTrue(res)
        
        res = signup.add_interest("liis@gmail.com", 2)
        self.assertIsNone(res)


if __name__ == "__main__":
    unittest.main()
