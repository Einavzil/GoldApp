import unittest
import sys, os
import mysql.connector
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import login

class test_login(unittest.TestCase):
    """Unit tests for login.py file."""
    
    def test_is_file_login(self):
        """Checks if the 'login.py' file exists."""
        res = os.path.isfile("src\login.py")
        exp = True
        self.assertEqual(res, exp)


    def test_connect(self):
        """Test the connection."""
        conn, cursor = login.connect()
        res = conn
        exp = mysql.connector.connection_cext.CMySQLConnection
        self.assertIsInstance(res, exp)
        
        res = cursor
        exp = mysql.connector.cursor_cext.CMySQLCursorPrepared
        self.assertIsInstance(res, exp)


    def test_check_email(self):
        """Test check email."""
        email = "liis@gmail.com"
        res = login.check_email(email)
        exp = True
        self.assertEqual(res, exp)
        
        email = "some@email.com"
        res = login.check_email(email)
        self.assertIsNone(res)
        
        res = login.check_email("kalle@gmail.com")
        self.assertEqual(res, None)
    

    def test_check_password(self):
        """Lets check the pass."""
        email = "liis@gmail.com"
        pw = "pass"
        res = login.check_password(email, pw)
        exp = True
        self.assertEqual(res, exp)
        
        pw = "1 = 1"
        res = login.check_password(email, pw)
        self.assertFalse(res)


    def test_decrypt_pass(self):
        """Test."""
        res = login.decrypt_pass
        self.assertTrue(res)
       
        
    def test_store_current_email(self):
        """Testing login functions."""
        with open("src\current_email.txt", "r") as login_file:
            original_email = login_file.readline()
        email = "hello@world.com"
        login.store_current_email(email)
        with open("src\current_email.txt", "r") as login_file:
            res = login_file.readline()
        exp = email
        self.assertEqual(res, exp)
        self.assertNotEqual(exp, original_email)
        login.store_current_email(original_email)
        with open("src\current_email.txt", "r") as login_file:
            old_email = login_file.readline()
        self.assertEqual(original_email, old_email)
        
        
        
   

if __name__ == "__main__":
    unittest.main()
