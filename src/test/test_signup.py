import os.path
import unittest
import sys
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import signup


class test_signup(unittest.TestCase):
    """Unit tests for signup.py file."""
    
    def test_is_file_signup(self):
        """Checks if the 'show_events.py' file exists."""
        res = os.path.isfile("src\signup.py")
        exp = True
        self.assertEqual(res, exp)


    def test_connect(self):
        """Test the connection."""
        connection = signup.connect()
        if connection == None:
            self.assertIsNone(connection)
            self.assertRaises(Exception, signup.connect)
        else:
            self.assertTrue(connection)


    def test_insert_account(self):
        """Testing if we can call the function."""
        res = signup.insert_account
        self.assertTrue(res)


    def test_get_location_id(self):
        """Let's get the location id."""
        location = "Stockholm"
        res = signup.get_location_id(location)
        exp = 2
        self.assertEqual(res, exp)


    def test_encrypt_pass(self):
        """Lets encrypt passwords."""
        passw = "password"
        res = signup.encrypt_pass(passw)
        exp = "password"
        self.assertIsNot(res, exp)
        

    def test_add_interest(self):
        """Test."""
        res = signup.add_interest
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
